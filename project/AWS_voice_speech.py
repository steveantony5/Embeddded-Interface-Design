import boto3
import pyaudio
import wave
import os
import aws_polly
import sqs_send
import py_camera
import time

def voice_to_text():
	print("Recording")
	os.system('arecord -d 3 -r 16000 -f S16_LE -t wav command.wav')
	print("processing")


	client = boto3.client('lex-runtime', region_name="us-east-1")

	#convert voice to speech
	obj = wave.open('command.wav','rb')
	response = client.post_content(
	    botName='eidproject',
	    botAlias='eidproject',
	    userId='test',
	    contentType='audio/l16; rate=16000; channels=1',
	    accept='text/plain; charset=utf-8',
	    inputStream=obj.readframes(96044)
	)
	    
	response_from_lex = response['message']
	print(response_from_lex)
	return response_from_lex


def wand_activate():
	if voice_to_text() == "identifio":
		#turn on camera
		print("label from aws")
		label = py_camera.get_label()
		print(label)
		time.sleep(5)
		aws_polly.text_to_voice(label)
		print("Microphone activated")
		print("Say Correcto or Wrongo")

		response = voice_to_text()
		
		if response == "correcto":
			sqsmsg = [{'label':label},{'command':'correcto'}]
			sqs_send.push_to_SQS(sqsmsg)

		elif response == "wrongo":
			sqsmsg = [{'label':label},{'command':'wrongo'}]
			sqs_send.push_to_SQS(sqsmsg)
		else:
			sqsmsg = [{'label':label},{'command':'invalid'}]
			sqs_send.push_to_SQS(sqsmsg)

