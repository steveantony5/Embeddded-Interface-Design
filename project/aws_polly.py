import boto3

polly_client = boto3.Session(region_name='us-east-1').client('polly')

response_polly = polly_client.synthesize_speech(VoiceId='Joanna',
                OutputFormat='mp3', 
                Text = 'Wand says ')
                
# Output the task ID
taskId = response['SynthesisTask']['TaskId']
print(f'Task id is {taskId}')

# Retrieve and output the current status of the task
task_status = polly_client.get_speech_synthesis_task(TaskId = taskId)
print(f'Status: {task_status}')
