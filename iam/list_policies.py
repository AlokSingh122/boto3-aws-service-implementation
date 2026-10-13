
import boto3
from botocore.exceptions import ClientError

try:
    iam = boto3.client("iam")
    paginator = iam.get_paginator("list_policies")

    for page in paginator.paginate(Scope="Local"):
        for policy in page["Policies"]:
            print("Policy name:", policy["PolicyName"])
            print("ARN:", policy["Arn"])
            print("Policy ID:", policy["PolicyId"])
            print("-" * 40)

except ClientError as error:
    print("Error:", error)
