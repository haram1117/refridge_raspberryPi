import logging
import boto3
from botocore.exceptions import ClientError
import os

def upload_file(file_name, bucket, object_name=None):
    
    s3 = boto3.resource('s3')
    s3_client = boto3.client('s3')
    s3_bucket = s3.Bucket(bucket)
    
    objectCount = sum(1 for _ in s3_bucket.objects.filter(Prefix='FoodImages/').all())
    
    if object_name is None:
        object_name = f'FoodImages/image{objectCount}.jpg'
    
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True
