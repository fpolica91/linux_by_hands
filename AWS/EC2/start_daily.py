import boto3


def lambda_handler(event, context):
    # TODO implement
    ec2 = boto3.resource('ec2')
    instances = ec2.instances.filter(
        Filters=[{'Name': 'instance-state-name', 'Values': ['stopped']}])

    for instance in instances:
        instance.start()
        print(f"Instance {instance.id} started")
    return True
