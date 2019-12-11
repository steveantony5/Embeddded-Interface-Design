import boto3
import json

# Get the service resource
sqs = boto3.client('sqs', region_name='us-east-1')

# Get the queue
queueUrl = "https://sqs.us-east-1.amazonaws.com/516035883487/wand.fifo"


#function to send messages to SQS
def push_to_SQS(msg):
	# Parse the JSON message 
	print("Msg sending to SQS" + str(msg))

	eventText = json.dumps(msg)

	#sending the message to SQS
	response = sqs.send_message(
	    QueueUrl=queueUrl,
	    MessageBody=eventText,
	    MessageGroupId='1'
	)

	print(response)




