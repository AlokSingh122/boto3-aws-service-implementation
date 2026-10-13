
# Optional: use a predefined bucket instead of prompting.
# To enable this, uncomment the next line and comment out the bucket_name
# input line below.
# bucket_name = "portfolio-122"

import boto3
from pathlib import Path
from botocore.exceptions import ClientError

bucket_name = input("Enter S3 bucket name: ").strip()
object_key = input("Enter S3 object key: ").strip()
destination = input("Enter local destination path: ").strip().strip('"')

path = Path(destination)

if not bucket_name or not object_key or not destination:
    print("Error: All fields are required.")
elif path.exists() and input(
    "Local file exists. Replace it? Type YES: "
).strip() != "YES":
    print("Download cancelled.")
else:
    try:
        path.parent.mkdir(parents=True, exist_ok=True)

        s3 = boto3.client("s3")
        s3.download_file(bucket_name, object_key, str(path))

        print("Download successful:", path)

    except (ClientError, OSError) as error:
        print("Error:", error)
