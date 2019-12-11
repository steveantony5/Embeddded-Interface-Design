import boto3
import json
# Get the service resource
sqs = boto3.client('sqs', region_name='us-east-1')

# Get the queue
queueUrl = "https://sqs.us-east-1.amazonaws.com/516035883487/wand.fifo"


event = [{'label':'eeeeeeeeen'},{'command':'edw'}]


# Parse the JSON message 
eventText = json.dumps(event)

response = sqs.send_message(
    QueueUrl=queueUrl,
    MessageBody=eventText,
    MessageGroupId='1'
)

print(response)