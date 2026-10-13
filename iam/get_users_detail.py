
import boto3
from botocore.exceptions import ClientError

username = input("Enter IAM username: ").strip()

if not username:
    print("Username cannot be empty.")
else:
    try:
        iam = boto3.client("iam")
        response = iam.get_user(UserName=username)
        user = response["User"]

        print("Username:", user["UserName"])
        print("User ID:", user["UserId"])
        print("ARN:", user["Arn"])
        print("Created:", user["CreateDate"])
        print("Path:", user["Path"])

    except ClientError as error:
        print("Error:", error)
