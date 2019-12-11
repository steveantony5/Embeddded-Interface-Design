'''Includes'''
import picamera as cam
import boto3

SOURCE_IMAgE_FILENAME = "IMG_3125.JPG"
image = cam.PiCamera()

'''Functions that activates the camera , uses AWS rekognition and gives a label'''
def get_label():
	
	image.vflip = True
	image.capture(SOURCE_IMAgE_FILENAME)

	client = boto3.client("rekognition", region_name='us-east-1')

	#upload the image to bucket
	# Create an S3 client
	S3_upld = boto3.client('s3')

	BUCKET_NAME = "datasteve"
	
	#uploading the image to S3 bucket
	S3_upld.upload_file(SOURCE_IMAgE_FILENAME, BUCKET_NAME, SOURCE_IMAgE_FILENAME)

	with open(SOURCE_IMAgE_FILENAME, "rb") as source_image:
	    source_bytes = source_image.read()

	response = client.detect_labels(Image={'Bytes': source_bytes},
	                                MaxLabels=1)

	return response['Labels'][0]['Name']
