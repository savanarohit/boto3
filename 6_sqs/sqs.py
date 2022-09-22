import boto3

# Creating a SQS Queue
sqs = boto3.resource('sqs')
queue = sqs.create_queue(QueueName='test_queue',
                         Attributes={'DelaySeconds': '5'})
print("Queue URL:", queue.url)
print("Queue Delay Seconds:", queue.attributes.get('DelaySeconds'))

# Getting SQS Queue details
# print(dir(sqs))
