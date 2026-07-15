import os
import boto3
from dotenv import load_dotenv
from botocore.exceptions import ClientError

load_dotenv()

AWS_REGION = os.getenv("AWS_REGION")
BUCKET = os.getenv("S3_BUCKET")

s3_client = boto3.client(
    "s3",
    region_name=AWS_REGION
)


def upload_to_s3(file):
    """
    Upload a file to Amazon S3.
    """

    try:

        s3_client.upload_fileobj(
            file.file,
            BUCKET,
            file.filename
        )

        return {
            "message": "File uploaded successfully",
            "file_name": file.filename
        }

    except ClientError as e:

        return {
            "error": e.response["Error"]["Message"]
        }