# AWS-CloudWatch-Automation

**Summary**

This project uses python to automate a notification system. The notification system uses CloudWatch to monitor traffic to an EC2 compute instance and invokes a Lambda function to notify an autoscaling group to add more compute resources. Notifications are then sent to a Slack Application. The goal of this project is to automate a notifcation system using AWS and python.

**Prerequisites**
- pipenv
- Ipython
- boto3
- AWS Account with 1 VPC created
- install httpd web server
- 

**Resources Used**

- AWS Lambda
- AWS SNS
- AWS CloudWatch/CloudWatch Logs
- AWS VPC configured with an Autoscaling group.
- Python
- Slack

**File Description**

- Pipfile Pipfile.lock - packages needed to run the pipenv environment
- autoscale.py - autscale commands to invoke function to scale-up/scale-down pipenv code
- config.tmpl.json - configuration template
- ec2_config.py - setting up a single ec2 instance and connecting through ssh
- scale-up.py - python commands to add EC2 instance.
- post_to_slack.py - code to send notifications to Slack
- notifier - folder containing AWS configuration files

**Program Procedure**

1. Setup the AWS environment with a single EC2 instance within a VPC and generated key pair (see ec2_confg.py for python commands). SSH into the created EC2 instance and use the commands in the scale-up.py file to test the connection by adding EC2 instances.

2. In the AWS console, delete the added instances in step 1, and attach an Autoscaling Group to the original EC2 instance. 

3. Configure the Autoscaling Group to scale up or down based on user defined thresholds.

4. In the EC2's ssh terminal: run 'stress -c 1 -t 600&' to stress test 1 EC2 instance for 10 min (600s). The background process can be viewed within terminal.

5. Use the commands in the autoscale.py file to scale-up or scale-down the EC2 resource.

6. Configure a Lambda function to send SNS topics to Slack when the CloudWatch alarm, setup in step 3, is triggerd.


