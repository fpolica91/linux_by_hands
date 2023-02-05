from datetime import datetime

import boto3


def lambda_handler(event, context):

    ec2 = boto3.resource('ec2')

    instances = ec2.instances.filter(
        Filters=[
            {'Name': 'tag:backup', 'Values': ['true']}
        ]
    )

    # ISO 8601 timestamp, i.e. 2019-01-31T14:01:58
    timestamp = datetime.utcnow().replace(microsecond=0).isoformat()

    for i in instances.all():
        for v in i.volumes.all():

            desc = 'Backup of {0}, volume {1}, created {2}'.format(
                i.id, v.id, timestamp)
            print(desc)

            snapshot = v.create_snapshot(Description=desc)

            print("Created snapshot:", snapshot.id)


# This is a Python function using the Boto3 library to create
# an Amazon Elastic Compute Cloud(EC2) snapshot for EC2 instances that are tagged with "backup: true".

# The function does the following:

# Creates an EC2 resource client using boto3.resource('ec2').
# Filters the instances that have the tag "backup: true" using `ec2.instances.filter(Filters=[{'Name': 'tag:backup', 'Values': ['true']}])`.
# Gets the current UTC time and formats it to an ISO string using datetime.utcnow().replace(microsecond=0).isoformat().
# Iterates over the filtered instances, and for each instance, iterates over its volumes and calls create_snapshot on each volume to create a snapshot.
# Prints the created snapshot ID for each snapshot.
# This function can be run in an AWS Lambda function or in a local environment with appropriate permissions.
