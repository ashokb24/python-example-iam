import boto3
import os


def hello(event, context):
    client = boto3.client("lambda")
    response = client.list_functions()
    env_variable = os.environ['FIRST_NAME']
    print('Environment Variable Value ' + env_variable)
    return response
