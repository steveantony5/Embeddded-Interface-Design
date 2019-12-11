#!/usr/bin/python3

import picamera as cam
import boto3

def get_label():
	image = cam.PiCamera()
	image.vflip = True
	image.capture('IMG_3125.JPG')

	img = "test.jpg"

	client = boto3.client("rekognition", region_name='us-east-1')

	#upload the image to bucket
	# Create an S3 client
	S3_upld = boto3.client('s3')

	BUCKET_NAME = "datasteve"
	SOURCE_FILENAME = "IMG_3125.JPG"

	S3_upld.upload_file(SOURCE_FILENAME, BUCKET_NAME, SOURCE_FILENAME)

	with open(img, "rb") as source_image:
	    source_bytes = source_image.read()

	response = client.detect_labels(Image={'Bytes': source_bytes},
	                                MaxLabels=1)

	return response['Labels'][0]['Name']
