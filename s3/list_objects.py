
# Optional: use a predefined bucket instead of prompting.
# To enable this, uncomment the next line and comment out the bucket_name
# input line below.
# bucket_name = "portfolio-122"

import boto3
from botocore.exceptions import ClientError

bucket_name = input("Enter bucket name: ").strip()

try:
    s3 = boto3.client("s3")
    paginator = s3.get_paginator("list_objects_v2")

    found = False

    for page in paginator.paginate(Bucket=bucket_name):
        for obj in page.get("Contents", []):
            found = True
            print("Key:", obj["Key"])
            print("Size:", obj["Size"], "bytes")
            print("Last modified:", obj["LastModified"])
            print("-" * 40)

    if not found:
        print("Bucket is empty or contains no matching objects.")

except ClientError as error:
    print("Error:", error)
