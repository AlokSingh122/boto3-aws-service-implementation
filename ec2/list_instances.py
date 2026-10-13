
import boto3
from botocore.exceptions import ClientError

try:
    ec2 = boto3.client("ec2")
    paginator = ec2.get_paginator("describe_instances")

    for page in paginator.paginate():
        for reservation in page["Reservations"]:
            for instance in reservation["Instances"]:
                print("Instance ID:", instance["InstanceId"])
                print("State:", instance["State"]["Name"])
                print("Type:", instance["InstanceType"])
                print("Private IP:", instance.get("PrivateIpAddress"))
                print("Public IP:", instance.get("PublicIpAddress"))
                print("-" * 40)

except ClientError as error:
    print("Error:", error)
