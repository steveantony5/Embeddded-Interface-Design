'''Includes'''
import boto3
import pyaudio
import wave
import os
import aws_polly
import sqs_send
import py_camera
import time
import dbhandler as db

database = r"eidproject.db"

'''Function which turns on the microphone and converts voice to Text using AWS Lex'''
def voice_to_text():
	print("Recording")

	#command to record
	os.system('arecord -d 3 -r 16000 -f S16_LE -t wav command.wav')
	print("processing")

	#creating lex instance
	robot = boto3.client('lex-runtime', region_name="us-east-1")

	#connection with lex robot
	obj = wave.open('command.wav','rb')
	response = robot.post_content(
	    botName='eidproject',
	    botAlias='eidproject',
	    userId='test',
	    contentType='audio/l16; rate=16000; channels=1',
	    accept='text/plain; charset=utf-8',
	    inputStream=obj.readframes(96044)
	)
	    
	#getting response from Lex robot
	response_from_lex = response['message']
	print(response_from_lex)
	return response_from_lex


'''function which wakes the wand and starts the entire application'''
def wand_activate():

	#need to turn the camera on if the voice was Identifio
	if voice_to_text() == "identifio":
		#turn on camera
		print("label from aws")

		#AWS rekognition return label for the photo
		label = py_camera.get_label()
		print(label)
		

		#convert text to speech
		aws_polly.text_to_voice(label)

		time.sleep(5)
		print("Microphone activated")
		print("Say Correcto or Wrongo")

		#pushes the data to SQS based on the response for the label

		response = voice_to_text()
		
		conn = db.create_connection(database)
		db.create_table(conn)
		
		
		if response == "righto":
			sqsmsg = [{'label':label},{'command':'righto'}]
			data_db = ("righto",label)
			
			sqs_send.push_to_SQS(sqsmsg)

		elif response == "wrongo":
			sqsmsg = [{'label':label},{'command':'wrongo'}]
			data_db = ("wrongo",label)
			
			sqs_send.push_to_SQS(sqsmsg)
		else:
			sqsmsg = [{'label':label},{'command':'invalid'}]
			data_db = ("invalid",label)
			
			sqs_send.push_to_SQS(sqsmsg)
			
		db.insert_data(conn, data_db)
		conn.commit()
		conn.close()

