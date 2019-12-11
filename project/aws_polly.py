import boto3
import pygame

polly_client = boto3.Session(region_name='us-east-1').client('polly')


'''Function to convert text to voice by AWS polly'''
def text_to_voice(text_ip):
	response = polly_client.synthesize_speech(VoiceId='Joanna',OutputFormat='mp3', Text = 'Wand says' + text_ip)
	                
	file = open('speech_polly.mp3', 'wb')
	file.write(response['AudioStream'].read())
	file.close()

	#command to play
	#os.system('aplay speech_polly.mp3')
	
	
	pygame.mixer.init()
	pygame.mixer.music.load("speech_polly.mp3")
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy() == True:
		continue
