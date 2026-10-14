
import json
from pathlib import Path

import boto3
from botocore.exceptions import BotoCoreError, ClientError

REGION = "ap-south-1"
OUTPUT_FILE = Path(__file__).with_name("lambda_inventory.json")


def list_lambda_functions():
    """List Lambda functions and extract selected details."""

    client = boto3.client("lambda", region_name=REGION)
    paginator = client.get_paginator("list_functions")

    functions = []

    for page in paginator.paginate():
        for function in page.get("Functions", []):
            functions.append({
                "FunctionName": function.get("FunctionName"),
                "Runtime": function.get("Runtime"),
                "MemorySize": function.get("MemorySize"),
                "Timeout": function.get("Timeout"),
                "FunctionArn": function.get("FunctionArn"),
                "LastModified": function.get("LastModified")
            })

    return functions


def main():
    try:
        functions = list_lambda_functions()

        json_output = json.dumps(functions, indent=4)

        print(json_output)

        OUTPUT_FILE.write_text(
            json_output + "\n",
            encoding="utf-8"
        )

        print(f"\nTotal functions: {len(functions)}")
        print(f"JSON report: {OUTPUT_FILE}")

    except ClientError as error:
        print(f"AWS API error: {error}")

    except BotoCoreError as error:
        print(f"AWS SDK error: {error}")

    except OSError as error:
        print(f"File error: {error}")


if __name__ == "__main__":
    main()
