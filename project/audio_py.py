import boto3
import pyaudio
import wave
import os


print("Recording")
os.system('arecord -d 3 -f S16_LE -r 48000 command.wav')

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
