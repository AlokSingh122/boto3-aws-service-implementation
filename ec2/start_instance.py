
# Optional example: launch a new EC2 instance with a predefined AMI ID.
# This example is not run by this script. Before enabling it, replace the
# placeholder with an AMI ID available in your configured AWS region.
# Launching an instance may incur AWS charges.
#
# ami_id = "ami-REPLACE_WITH_YOUR_AMI_ID"
# ec2 = boto3.client("ec2")
# response = ec2.run_instances(
#     ImageId=ami_id,
#     InstanceType="t2.micro",
#     MinCount=1,
#     MaxCount=1,
# )
# print("Launched instance:", response["Instances"][0]["InstanceId"])

import boto3
from botocore.exceptions import ClientError

instance_id = input("Enter instance ID to start: ").strip()

if input(f"Start {instance_id}? Type YES: ").strip() == "YES":
    try:
        ec2 = boto3.client("ec2")
        response = ec2.start_instances(InstanceIds=[instance_id])

        for instance in response["StartingInstances"]:
            print(instance["InstanceId"], instance["CurrentState"]["Name"])

    except ClientError as error:
        print("Error:", error)
else:
    print("Operation cancelled.")
