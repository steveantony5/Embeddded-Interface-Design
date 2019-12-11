import boto3

polly_client = boto3.Session(region_name='us-east-1').client('polly')

response = polly_client.synthesize_speech(VoiceId='Joanna',OutputFormat='mp3', Text = 'steve steve ')
                
file = open('speech.mp3', 'wb')
file.write(response['AudioStream'].read())
file.close()
