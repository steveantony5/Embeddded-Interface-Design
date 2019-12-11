#includes
from PyQt5 import QtWidgets, QtGui,QtCore
from project import Ui_Dialog #importing the generated python class from.ui
from PyQt5.QtWidgets import QTableWidgetItem
import  random
import sys
import time

import boto3
import json

#instance of SQS
sqs = boto3.client('sqs', region_name='us-east-1')

queueUrl = "https://sqs.us-east-1.amazonaws.com/516035883487/wand.fifo"

#instance of S3 bucket
s3 = boto3.resource('s3', region_name='us-east-1')
BUCKET_NAME = "datasteve"
Image_name = "IMG_3125.JPG"

#variable for calculating the analysis
voice_cmd_correct = 0
Image_recog_correct = 0
total_messages = 0
percentage_voice_recog = 0
precentage_image_correct = 0

#inheriting mywindow class from the class QDialog
class mywindow(QtWidgets.QDialog):
    def __init__(self):
        '''Constructor for the class'''
        super(mywindow, self).__init__() #initiating the parent class
        self.ui = Ui_Dialog()
        self.ui.setupUi(self) #calling the function generated in the .ui

        self.ui.pushButton.clicked.connect(self.last_image)

        self.ui.pushButton_2.clicked.connect(self.analysis)

    #function to display the latest clicked image on GUI
    def last_image(self):

        #download the latest image from S3 bucket
        s3.Bucket(BUCKET_NAME).download_file(Image_name, 'my_local_image.jpg')
        self.ui.photo.setPixmap(QtGui.QPixmap("my_local_image.jpg"))


    #function which displays analytics details on GUI
    def analysis(self):
        global voice_cmd_correct
        global Image_recog_correct
        global total_messages
        global percentage_voice_recog
        global precentage_image_correct
        while 1:

            try:
                #receive the messages from SQS
                response = sqs.receive_message(QueueUrl=queueUrl,MaxNumberOfMessages=1)
                message = response['Messages']
                data = json.loads(message[0]['Body'])

                #delete the message from SQS
                sqs.delete_message(QueueUrl=queueUrl, ReceiptHandle=message[0]['ReceiptHandle'])

                #have a message count for tracking percentage
                total_messages = total_messages+1

                #correcto voice commands on SQS
                if data[1]['command'] == "Correcto":
                    print("Correcto received")
                    Image_recog_correct = Image_recog_correct +1
                    voice_cmd_correct = voice_cmd_correct +1

                #wrongo voice commands on SQS
                elif data[1]['command'] == "Wrongo":
                    print("Wrongo received")
                    voice_cmd_correct = voice_cmd_correct+1

                    #decrement the correct count only if it is greater than 0
                    if Image_recog_correct>1:
                        Image_recog_correct = Image_recog_correct+1

                #unrecognized voice commands on SQS
                else:
                    print("Wrong voice command")
                    #decrement the voice correct command only if t is greater than 0
                    if voice_cmd_correct > 1:
                        voice_cmd_correct = voice_cmd_correct - 1

            except:
                print("No more messages")
                break

        #calculate the percentage of Voice recognized
        percentage_voice_recog = (voice_cmd_correct / total_messages) * 100

        #calculate the percentage of image correct
        precentage_image_correct = (Image_recog_correct / total_messages) * 100

        #display the percentage on GUI
        self.ui.lineEdit_image.setText(str(precentage_image_correct))
        self.ui.lineEdit_voice.setText(str(percentage_voice_recog))



def main():
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()
    app.exec() # to execute the application


if __name__ == '__main__':
    main()
