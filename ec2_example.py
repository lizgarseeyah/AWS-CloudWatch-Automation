# coding: utf-8
import boto3
session = boto3.Session(profile_name='pythonAutomation')
ec2 = session.resource('ec2')
key_name = 'python_automation_key'
key_path = key_name + '.pem'
key = ec2.create_key_pair(KeyName=key_name)
key.key_material
with open(key_path, 'w') as key_file:
    key_file.write(key.key_material)
    
get_ipython().run_line_magic('ls', '-l python_automation_key.pem')
import os, stat
os.chmod(key_path, stat.S_IRUSR | stat.S_IWUSR)
import boto3
session = boto3.Session(profile_name='pythonAutomation')
ec2 = session.resource('ec2')
key_name = 'python_automation_key'
key_path = '/Users/lizgarcia/Desktop/ROADMAP/AWS/automating-aws-w-python/notifications-for-cloud-watch-events/key/python_automation_key.pem'
key = ec2.create_key_pair(KeyName=key_name)
key.key_material
with open(key_path, 'w') as key_file:
    key_file.write(key.key_material)
    
with open(key_path, 'w') as key_file:
    key_file.write(key.key_material)
    
with open(key_path, 'w') as key_file:
    key_file.write(key.key_material)
    
get_ipython().run_line_magic('clear', '')
import boto3
session = boto3.Session(profile_name='pythonAutomation')
ec2 = session.resources('ec2')
ec2 = session.resource('ec2')
key_name = 'python_automation_key'
key_path = key_name + '.pem'
key.key_material
with open(key_path, 'w') as key_file:
    key_file.write(key.key_material)
    
get_ipython().run_line_magic('ls', '-l python_automation_key.pem')
import os, stat
os.chmod(key_path, stat.S_IRUSR | stat.S_IWUSR)
get_ipython().run_line_magic('ls', '-l python_automation_key.pem')
ec2.images.filter(Owners=['amazon'])
list(ec2.images.filter(Owners=['amazon']))
len(list(ec2.images.filter(Owners=['amazon])))
len(list(ec2.images.filter(Owners=['amazon'])))
img = ec2.Image('ami-02354e95b39ca8dec')
img.name
ec2_apse2 = session.resource('ec2', region_name='ap-northeast-1')
img_apse2 = ec2_apse2.Image('ami-02354e95b39ca8dec')
img_apse2.name
img.name
ami_name = 'amzn2-ami-hvm-2.0.20200722.0-x86_64-gp2'
filters = [{'Name': 'name', 'Values': [ami_name]}]
list(ec2.images.filter(Owners=['amazon'], Filters = filters))
list(ec2_apse2.images.filter(Owners=['amazon'], Filters = filters))
instances = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key.key_name)
instances
ec2.Instance(id='i-0b0f9cbee207c7807')
inst = instances[0]
inst.public_dns_name
inst.wait_until_running()
inst.reload()
inst.public_dns_name
inst.security_groups
# Look up the security group
# Authorize incoming connections from our public IP address, on port 22 (the port SSH uses)
sg = ec2.SecurityGroup(inst.security_groups[0]['GroupId'])
sg.authorize_ingress(IpPermissions=[{'FromPort': 22, 'ToPort': 22, 'IpProtocol':'TCP', 'IpRanges': [{'CidrIp':'207.212.57.238'}]}])
sg.authorize_ingress(IpPermissions=[{'FromPort': 22, 'ToPort': 22, 'IpProtocol':'TCP', 'IpRanges': [{'CidrIp':'207.212.57.238/32'}]}])
sg.authorize_ingress(IpPermissions=[{'FromPort': 80, 'ToPort': 80, 'IpProtocol':'TCP', 'IpRanges': [{'CidrIp':'0.0.0.0/0'}]}])
inst.public_dns_name
sg = ec2.SecurityGroup(inst.security_groups[0]['GroupId'])
sg.authorize_ingress(IpPermissions=[{'FromPort': 22, 'ToPort': 22, 'IpProtocol':'TCP', 'IpRanges': [{'CidrIp':'207.212.57.238/32'}]}])
sg.authorize_ingress(IpPermissions=[{'FromPort': 80, 'ToPort': 80, 'IpProtocol':'TCP', 'IpRanges': [{'CidrIp':'0.0.0.0/0'}]}])
inst.public_dns_name
get_ipython().run_line_magic('history', '')
get_ipython().run_line_magic('save', '1-46 ec2_example.py')
get_ipython().run_line_magic('save', 'ec2_example.py 1-71')
