
import boto3
from botocore.exceptions import BotoCoreError, ClientError

def check_aws_configuration():
    try:
        session = boto3.Session()
        region = session.region_name

        if not region:
            print("ERROR: AWS region is not configured.")
            print("Run: aws configure")
            return

        sts = session.client("sts")
        identity = sts.get_caller_identity()

        print("AWS configuration verified successfully!")
        print("Account ID:", identity["Account"])
        print("Caller ARN:", identity["Arn"])
        print("User ID:", identity["UserId"])
        print("Configured region:", region)

        print("\nChecking service client creation...")
        for service in ["iam", "ec2", "s3"]:
            session.client(service)
            print(f"{service.upper()}: Client created")

        print("\nNote: Client creation does not verify service permissions.")

    except (BotoCoreError, ClientError) as error:
        print("AWS configuration check failed:", error)

if __name__ == "__main__":
    check_aws_configuration()
