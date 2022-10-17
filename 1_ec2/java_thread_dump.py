# Program to run bash shell commands (Taking Java Thread Dump) in an EC2 Instance using SSM (Systems Manager Agent) and save it to a S3 Bucket.
# First install ssm agent on EC2 and then attach SSM IAM policy to it.
# import botocore
import boto3
# import time

# SSM Agent Session with bash shell commands
# def lambda_handler(event, context):
ssm_client = boto3.client('ssm')
response = ssm_client.send_command(
    InstanceIds=['i-0d55cdb9e4251c405'],
    DocumentName="AWS-RunShellScript",
    Parameters={
        'commands': ['PID=$(sudo pgrep java) && sudo -u tomcat jstack -l $PID > /tmp/thread.txt']
    },

)


#print("Thread dumped into /tmp dir")

# read -p "Enter FCO Number:" fco
