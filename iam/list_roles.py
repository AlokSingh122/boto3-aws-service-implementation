
import boto3
from botocore.exceptions import ClientError

try:
    iam = boto3.client("iam")
    paginator = iam.get_paginator("list_roles")

    for page in paginator.paginate():
        for role in page["Roles"]:
            print("Role name:", role["RoleName"])
            print("ARN:", role["Arn"])
            print("Created:", role["CreateDate"])
            print("-" * 40)

except ClientError as error:
    print("Error:", error)
