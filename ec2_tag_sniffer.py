#!/usr/bin/env python
'''A simple script to parse and delete tags in AWS-EC2 using boto3'''
import boto3

# Print menu for region list
print("\n||| Welcome to EC2 tag sniffer v1.0 |||")

print("""
af-south-1
ap-east-1
ap-northeast-1
ap-northeast-2
ap-northeast-3
ap-south-1
ap-southeast-1
ap-southeast-2
ca-central-1
eu-central-1
eu-north-1
eu-south-1
eu-west-1
eu-west-2
eu-west-3
me-south-1
sa-east-1
us-east-1
us-east-2
us-west-1
us-west-2
""")

while True:
    # Obtain user input for region and tag
    region = input("Which region would you like to scan?: ").lower()
    if region in ('af-south-1', 'ap-east-1', 'ap-northeast-1', 'ap-northeast-2', 'ap-northeast-3',
                  'ap-south-1', 'ap-southeast-1', 'ap-southeast-2', 'ca-central-1', 'eu-central-1',
                  'eu-north-1', 'eu-south-1', 'eu-west-1', 'eu-west-2', 'eu-west-3', 'me-south-1',
                  'sa-east-1', 'us-east-1', 'us-east-2', 'us-west-1', 'us-west-2'):
        pass
    else:
        continue
    key_to_find = input(
        "\nWhat is the tag KEY you are looking to find? (case sensitive): ")

    print("")

    # Set boto3.resource to ec2 in proper region - parse instances with tag filter
    ec2 = boto3.resource('ec2', region_name=region)

    instance_ids = []

    for instance in ec2.instances.all():
        name = ''
        tags = {}
        for tag in instance.tags:
            if tag['Key'] == key_to_find:
                instance_ids.append(instance.instance_id)

    if not instance_ids:
        print(f"The tag '{key_to_find}' was not found in {region}\n")
        print("Please try again\n")
        continue

    if instance_ids is not None:
        for id in instance_ids:
            print(f"Instance {id} has the tag || {key_to_find} ||")
        break

# Ask user if they want to proceed with deleting found tags - else exit
deleteme = input(
    "\nWould you like to delete this tag from the instances? (y/n): ").lower()
if deleteme == "y":
    print("\nNow deleting the tag for each instance id.\n")
    for id in instance_ids:
        tagRes = boto3.client('ec2', region_name=region)
        ret = tagRes.delete_tags(
            Resources=[id],
            Tags=[{'Key': key_to_find}]
        )
        print(f"Instance tag || {key_to_find} || removed for {id}.")
else:
    exit()
