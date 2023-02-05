import boto3


def lambda_handler(event, context):
    # get list of regions
    ec2 = boto3.resource('ec2')
    instances = ec2.instances.filter(
        Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

    for instance in instances:
        instance.stop()
        print("stopped instance")

    return True
