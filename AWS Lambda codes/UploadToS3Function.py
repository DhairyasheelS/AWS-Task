import json
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    # Extracting file details from the event
    bucket_name = event.get('bucket_name')
    file_name = event.get('file_name')
    file_content = event.get('file_content')  # Base64-encoded content of the document

    # Validate if all necessary parameters are provided
    if not all([bucket_name, file_name, file_content]):
        return {
            'statusCode': 400,
            'body': json.dumps('bucket_name, file_name, and file_content are required.')
        }

    try:
        # Uploading the file to the S3 bucket
        s3_client.put_object(Bucket=bucket_name, Key=file_name, Body=file_content, ContentType='application/pdf')
        
        return {
            'statusCode': 200,
            'body': json.dumps(f'File {file_name} successfully uploaded to {bucket_name}')
        }
    except (NoCredentialsError, PartialCredentialsError) as e:
        return {
            'statusCode': 403,
            'body': json.dumps(f'Credentials issue: {str(e)}')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error uploading file: {str(e)}')
        }
