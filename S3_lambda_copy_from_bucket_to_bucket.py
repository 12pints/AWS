# working 17 august 2021
# this code is triggered by an S3 ObjetcPUT event.
# as soon as the object is added to the source bucket, it will copy it to the destination bucket (danish-tst-backup-bucket)
# source:  https://www.powerupcloud.com/copying-objects-using-aws-lambda-based-on-s3-events-part-1/
# described in: https://ciscoshizzle.blogspot.com/2021/08/aws-lambda-function-automatic-backup.html

import json
import boto3

# boto3 S3 initialization
s3_client = boto3.client("s3")

def lambda_handler(event, context):
   destination_bucket_name = 'danish-tst-backup-bucket'

   # event is a dictionary and contains all information about newly uploaded object
   print("Event :", event)

   # Bucket Name where file was uploaded, obtained from event dictionary
   source_bucket_name = event['Records'][0]['s3']['bucket']['name']

   # Filename of object (with path), obtained from event dictionary
   file_key_name = event['Records'][0]['s3']['object']['key']

   # Copy Source Object
   copy_source_object = {'Bucket': source_bucket_name, 'Key': file_key_name}

   # S3 copy object operation, note file_key_name remains same in source and destination
   s3_client.copy_object(CopySource=copy_source_object, Bucket=destination_bucket_name, Key=file_key_name)

   return {
       'statusCode': 200,
       'body': json.dumps('Hello from S3 events Lambda!')
   }
