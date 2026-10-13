
import boto3
from botocore.exceptions import ClientError

# Optional: use a predefined EC2 instance ID instead of prompting.
# Replace the example ID with your instance ID, uncomment this assignment,
# and comment out the input() line below to enable it.
# instance_id = "i-0123456789abcdef0"

instance_id = input("Enter EC2 instance ID: ").strip()

try:
    ec2 = boto3.client("ec2")
    response = ec2.describe_instances(InstanceIds=[instance_id])

    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            print("Instance ID:", instance["InstanceId"])
            print("State:", instance["State"]["Name"])
            print("Type:", instance["InstanceType"])
            print("AMI ID:", instance["ImageId"])
            print("AZ:", instance["Placement"]["AvailabilityZone"])
            print("Private IP:", instance.get("PrivateIpAddress"))
            print("Public IP:", instance.get("PublicIpAddress"))
            print("Launch time:", instance.get("LaunchTime"))

except ClientError as error:
    print("Error:", error)
