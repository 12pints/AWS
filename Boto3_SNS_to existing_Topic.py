#This current code works october 2021
#
#
# this code is will send a message out ot a pre existing SNS topic
# Very basic code.
#
# boto3 library:  https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html
# source:  https://www.kodyaz.com/aws/send-sns-notification-from-aws-lambda-function-using-python.aspx

import os
import boto3
import json
from botocore.config import Config

my_config = Config(
    region_name = 'ap-southeast-2'
)

AWS_access_key = os.getenv('AWS_Python_access_key')
AWS_secret_access_key = os.getenv('AWS_Python_secret_access_key')

notification = "Here is the SNS notification for Lambda function tutorial."

#client = boto3.client('sns')

client = boto3.client('sns',
                      aws_access_key_id = AWS_access_key,
                      aws_secret_access_key = AWS_secret_access_key,
                      config=my_config)

response = client.publish (
      TargetArn = "arn:aws:sns:ap-southeast-2:281130355805:S3LambdaBucketCopy",
      Message = json.dumps({'default': json.dumps(notification),
                            'email': notification
                            }),
      MessageStructure='json'
         )
print('Finished execution')



