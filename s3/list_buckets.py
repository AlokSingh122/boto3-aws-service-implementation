
import boto3
from botocore.exceptions import ClientError

try:
    s3 = boto3.client("s3")
    response = s3.list_buckets()

    for bucket in response["Buckets"]:
        print("Bucket name:", bucket["Name"])
        print("Created:", bucket["CreationDate"])
        print("-" * 40)

except ClientError as error:
    print("Error:", error)
