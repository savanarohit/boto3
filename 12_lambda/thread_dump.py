# Program to run bash shell commands (Taking Java Thread Dump) in an EC2 Instance using SSM (Systems Manager Agent) and copy it to a S3 Bucket. First install ssm agent on EC2 and also attach SSM IAM policy to it.
import boto3


def lambda_handler(event, context):
    ssm_client = boto3.client('ssm')
    response = ssm_client.send_command(
        InstanceIds=['i-0d55cdb9e4251c405'],
        DocumentName="AWS-RunShellScript",
        Parameters={
            'commands': ['PID=$(sudo pgrep java) && sudo -u tomcat jstack -l $PID > /tmp/thread2.txt && cd /tmp && aws s3 cp thread2.txt s3://company-depolyment-bucket']
        },
    )
    return {
        'Status': "Success"
    }
