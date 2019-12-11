import boto3

polly_client = boto3.Session(region_name='us-east-1').client('polly')


def text_to_voice(text_ip):
	response = polly_client.synthesize_speech(VoiceId='Joanna',OutputFormat='mp3', Text = 'Wand says' + text_ip)
	                
	file = open('speech.mp3', 'wb')
	file.write(response['AudioStream'].read())
	file.close()
