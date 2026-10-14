import argparse
from pathlib import Path

import boto3
import yaml
from botocore.exceptions import ClientError


def load_users(config_path):
    with config_path.open(encoding="utf-8") as config_file:
        config = yaml.safe_load(config_file)

    if not isinstance(config, dict) or not isinstance(config.get("users"), list):
        raise ValueError("YAML must contain a 'users' list.")

    users = config["users"]
    for index, user in enumerate(users, start=1):
        if not isinstance(user, dict):
            raise ValueError(f"User entry {index} must be a mapping.")

        username = user.get("username")
        groups = user.get("groups", [])
        if not isinstance(username, str) or not username.strip():
            raise ValueError(f"User entry {index} must have a non-empty username.")
        if not isinstance(groups, list) or any(
            not isinstance(group, str) or not group.strip() for group in groups
        ):
            raise ValueError(
                f"Groups for user '{username}' must be a list of non-empty names."
            )

    return users


def main():
    parser = argparse.ArgumentParser(
        description="Create IAM users and add them to groups listed in a YAML file."
    )
    parser.add_argument(
        "config",
        nargs="?",
        type=Path,
        default=Path(__file__).with_name("users.yaml"),
        help="YAML config path (default: iam/users.yaml)",
    )
    args = parser.parse_args()

    try:
        users = load_users(args.config)
    except (OSError, yaml.YAMLError, ValueError) as error:
        parser.error(f"Could not load user configuration: {error}")

    if not users:
        print("No users found in the configuration.")
        return

    print(f"About to create or update group membership for {len(users)} IAM user(s).")
    if input("Continue? [y/N]: ").strip().lower() != "y":
        print("Cancelled.")
        return

    iam = boto3.client("iam")
    for user in users:
        username = user["username"].strip()
        try:
            iam.create_user(UserName=username)
            print(f"Created user: {username}")
        except ClientError as error:
            if error.response["Error"]["Code"] == "EntityAlreadyExists":
                print(f"User already exists: {username}")
            else:
                print(f"Could not create user '{username}': {error}")
                continue

        for group in user.get("groups", []):
            group_name = group.strip()
            try:
                iam.add_user_to_group(GroupName=group_name, UserName=username)
                print(f"Added {username} to group {group_name}")
            except ClientError as error:
                print(f"Could not add {username} to group '{group_name}': {error}")


if __name__ == "__main__":
    main()
