# Magic Wand

### Introduction
Magic Wand helps you to detect object and tell what it is using AWS. You can activate the magic wand by saying 'Identifio'.
Also you can evaluate the performance of the magic wand by saying 'Correcto' or 'Wrongo'. 
This helps to perform an analysis on how well the wand works which is being displayed on the PyQT GUI.

We use the following services

Text to Speech -> AWS Polly

Spech to Text -> AWS Lex

Image Recogniztion -> AWS Rekognition

For storing image, voice file -> AWS S3 bucket

Queueing messges like a databse -> AWS SQS

Local database -> SQLLite

Push button is provided on the wand which turns on the microphone.

### Project Developers
  - Steve Antony Xavier Kenndy
  - Sorabh Gandhi

### Project Work
1.) Steve Antony Xavier Kenndy - QT Design, AWS Polly, AWS Lex, SQS

2.)Sorabh Gandhi - Pi Camera, node js, Database, push button

### Installation
Install all the dependencies to run this project. Follow the installation instructions given below,

```sh
$ pip3 install boto3
$ sudo apt-get python3-pyaudio
```

### Run Steps
Run the shell script to kick the application running
```sh
$ bash kickoff.sh
```

#### Files in repository
Application.py -> GUI created using PyQt designer

project.py -> python script of the gui created using Pyqt5 designer on Ubuntu

dbhandler.py -> Functions related to database

AWS_voice_speech.py -> Functions related to AWS Lex

py_camera.py -> Functions related to picamera and AWS Rekognition

sqs_send.py -> Function which puts to AWS SQS

AWS_polly.py -> Functions related to Text to Voice in AWS Polly

kickoff.sh -> The script whichs runs the magic wand application

button.py -> Function related to button

.asoundrc -> Setting up the microphone as default. Should be resent in the root folder

#### References

#####AWS services
AWS Documentation and Python examples

https://medium.com/@likhita507/conversion-of-text-to-speech-speech-to-text-using-cloud-services-5189f508bc9
https://www.youtube.com/watch?v=KTa1T14nkbw
https://www.youtube.com/watch?v=PLnRzHNmcao

#####Setting up microphone on Rpi

http://jonamiki.com/2019/07/04/sound-on-raspberry-pi-separate-speaker-and-microphone/

#####PyQT Image display

https://www.youtube.com/watch?v=D0iCHFXHb_g


Note:
To change the resolution fit to screen on VNC server 
edit the follow
/boot/config.txt
hdmi_force_hotplug=1

hdmi_group=2
hdmi_mode=58
