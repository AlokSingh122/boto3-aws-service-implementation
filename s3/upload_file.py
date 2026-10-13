
# Optional: use a predefined bucket instead of prompting.
# To enable this, uncomment the next line and comment out the bucket_name
# input line below.
# bucket_name = "portfolio-122"

import boto3
from pathlib import Path
from botocore.exceptions import ClientError

file_path = input("Enter local file path: ").strip().strip('"')
bucket_name = input("Enter S3 bucket name: ").strip()
object_key = input("Enter destination object key: ").strip()

path = Path(file_path)

if not path.is_file():
    print("Error: Local file does not exist.")
elif not bucket_name or not object_key:
    print("Error: Bucket name and object key are required.")
else:
    try:
        s3 = boto3.client("s3")

        try:
            s3.head_object(Bucket=bucket_name, Key=object_key)
            exists = True
        except ClientError as error:
            status = error.response.get("ResponseMetadata", {}).get(
                "HTTPStatusCode"
            )
            code = error.response.get("Error", {}).get("Code")

            if status == 404 or code in ("404", "NoSuchKey", "NotFound"):
                exists = False
            else:
                raise

        if exists:
            confirm = input(
                "Object exists. Replace it? Type YES: "
            ).strip()
        else:
            confirm = "YES"

        if confirm == "YES":
            s3.upload_file(str(path), bucket_name, object_key)
            print("Upload successful:", object_key)
        else:
            print("Upload cancelled.")

    except ClientError as error:
        print("Error:", error)
