# boto3 AWS Examples

Small interactive Python scripts for working with AWS S3, EC2, and IAM through
the AWS SDK for Python (`boto3`).

## Requirements

- Python installed and available in PowerShell as `python` (or `py`).
- AWS credentials and a default region configured for the account you want to use.
- Permissions in AWS for the operations you run.

Install the project dependency from the project directory:

```powershell
python -m pip install -r requirements.txt
```

Using `python -m pip` runs pip through Python, so it works even when the standalone
`pip` command is not on `PATH`. If `python` is not recognized, try `py -m pip`.

Configure credentials and a default region with the AWS CLI if it is installed:

```powershell
aws configure
```

The scripts use boto3's standard credential chain. Do not put AWS access keys in
this README or commit credentials to the project.

## Running scripts

In PowerShell, first change to the project directory:

```powershell
cd C:\Users\ASUS\Desktop\SDK\boto3-aws
```

Run a script as a module from this directory with `python -m package.module`.
The module name follows the script's filename, without `.py`.

For example, to inspect an EC2 instance:

```powershell
python -m ec2.get_instance_detail
```

The filename is `get_instance_detail.py` (singular). The command
`python -m ec2.get_instance_details` fails because there is no module with that
plural name.

## Script commands

Run these from the project directory:

| Command | Purpose |
| --- | --- |
| `python aws_config_check.py` | Verify that AWS credentials and a region are available, show the caller identity, and test creation of IAM, EC2, and S3 clients. Client creation does not verify service permissions. |
| `python -m s3.list_buckets` | List buckets visible to the configured AWS identity. |
| `python -m s3.list_objects` | List objects in a bucket; prompts for the bucket name. |
| `python -m s3.upload_file` | Upload a local file; prompts for its path, the bucket, and the destination object key. |
| `python -m s3.download_file` | Download an S3 object; prompts for the bucket, object key, and local destination path. |
| `python -m ec2.list_instances` | List EC2 instances visible in the configured region. |
| `python -m ec2.get_instance_detail` | Show details for an EC2 instance; prompts for its instance ID. |
| `python -m ec2.start_instance` | Start an EC2 instance after confirmation; prompts for its instance ID. |
| `python -m ec2.stop_instance` | Stop an EC2 instance after confirmation; prompts for its instance ID. |
| `python -m iam.list_users` | List IAM users. |
| `python -m iam.get_users_detail` | Show details for an IAM user; prompts for the username. |
| `python -m iam.list_roles` | List IAM roles. |
| `python -m iam.list_policies` | List locally managed IAM policies. |

## S3 names and download paths

- **Bucket name** identifies the S3 bucket, for example `portfolio-122`.
- **Object key** identifies the object inside the bucket, for example
  `myfile.pdf` or `reports/january.csv`. It is not a local Windows path.
- **Local destination path** is where the downloaded file is saved. Include a
  filename, for example `C:\Users\ASUS\Downloads\myfile.pdf`, not just the
  `Downloads` folder.

Example download:

1. Run `python -m s3.download_file`.
2. Enter `portfolio-122` for the bucket if that is the bucket containing your file.
3. Enter the exact object key shown in S3, such as `reports/myfile.pdf`.
4. Enter `C:\Users\ASUS\Downloads\myfile.pdf` as the local destination.

An S3 object key is case-sensitive and may contain `/` to represent prefixes
(folders) in the S3 console. The download script creates local parent folders
when needed and asks for confirmation before replacing an existing local file.

## Safety and permissions

These scripts operate on the AWS account and region selected by your credentials
and configuration. The start/stop and file-transfer scripts can change AWS
resources or local files. Review the prompts and grant only the AWS permissions
needed for the operations you intend to use.
