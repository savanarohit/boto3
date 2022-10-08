# program to run operating system commands in an EC2 Instance
import boto3
import time

ssm_client = boto3.client('ssm')
response = ssm_client.send_command(
    InstanceIds=['i-0d07f0bcdfd129edc'],
    DocumentName="AWS-RunShellScript",
    Parameters={
        'commands': ['yum -y update && yum -y upgrade ']
    }, )

time.sleep(2)
command_id = response['Command']['CommandId']
output = ssm_client.get_command_invocation(
    CommandId=command_id,
    InstanceId='i-0d07f0bcdfd129edc',
)
print(output)
