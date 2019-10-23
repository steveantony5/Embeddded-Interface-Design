from __future__ import print_function
  
import json
import boto3
  
print('Loading function')
  
def lambda_handler(event, context):

	# Create an SNS client
    sns = boto3.client('sns')
	
	#Create an SQS client
    sqs = boto3.resource('sqs')
  
    # Parse the JSON message 
    eventText = json.dumps(event)
    
    # Print the parsed JSON message to the console; you can view this text in the Monitoring tab in the Lambda console or in the CloudWatch Logs console
    print('Received event: ', eventText) 
    
	# Check if the event type is an Alert
    if event['type']=='Alert':
      # Publish a message to the specified topic
      response = sns.publish (
	  # Send the alert to the specified mobile number and email address
        TopicArn = 'arn:aws:sns:us-east-1:516035883487:TestTopic',
        Message = eventText
      )
	  #Print the message on console
      print(response)
      
    else:
     queue = sqs.get_queue_by_name(QueueName='Steve_queue')
	 # Store the message in the specified Queue
     response = queue.send_message(MessageBody=json.dumps(event))