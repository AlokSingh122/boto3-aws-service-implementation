
import boto3
from botocore.exceptions import ClientError

instance_id = input("Enter instance ID to stop: ").strip()

if input(f"Stop {instance_id}? Type YES: ").strip() == "YES":
    try:
        ec2 = boto3.client("ec2")
        response = ec2.stop_instances(InstanceIds=[instance_id])

        for instance in response["StoppingInstances"]:
            print(instance["InstanceId"], instance["CurrentState"]["Name"])

    except ClientError as error:
        print("Error:", error)
else:
    print("Operation cancelled.")
