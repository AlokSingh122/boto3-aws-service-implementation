
import boto3
from botocore.exceptions import ClientError

try:
    iam = boto3.client("iam")
    paginator = iam.get_paginator("list_users")

    for page in paginator.paginate():
        for user in page["Users"]:
            print("Username:", user["UserName"])
            print("User ID:", user["UserId"])
            print("ARN:", user["Arn"])
            print("Created:", user["CreateDate"])
            print("-" * 40)

except ClientError as error:
    print("Error:", error)
