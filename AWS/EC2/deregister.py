import datetime
from dateutil.parser import parse
import boto3


def days_old(date):
    parsed = parse(date).replace(tzinfo=None)
    diff = datetime.datetime.now() - parsed
    return diff.days


def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    amis = ec2.describe_images(Owners=['self'])['Images']

    for ami in amis:
        creation_date = ami['CreationDate']
        age_days = days_old(creation_date)
        image_id = ami['ImageId']
        if age_days >= 2:
            print("deleting imageId", image_id)
            ec2.deregister_image(ImageId=image_id)
