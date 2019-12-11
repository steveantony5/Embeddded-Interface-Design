#!/usr/bin/python3

import picamera as cam
import boto3

def get_label():
	image = cam.PiCamera()
	image.vflip = True
	image.capture('test.jpg')

	img = "test.jpg"

	client = boto3.client("rekognition", region_name='us-east-1')

	with open(img, "rb") as source_image:
	    source_bytes = source_image.read()

	response = client.detect_labels(Image={'Bytes': source_bytes},
	                                MaxLabels=1)

	return response['Labels'][0]['Name']
