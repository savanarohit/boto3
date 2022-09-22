import boto3

region = 'ap-south-1'
client = boto3.client('ec2', region_name=region)
client.create_image(InstanceId='i-0c737dff3207221a3',
                    Name="DevOps", NoReboot=True)

region = 'ap-south-1'
client = boto3.client('ec2', region_name=region)
client.create_image(InstanceId='i-0420a9f9faa8f14e7',
                    Name="UbuntuDev", NoReboot=True)

client = boto3.client('ec2', region_name=region)
client.create_image(InstanceId='i-06a2dfcd94f1c952d',
                    Name="Docker", NoReboot=True)
