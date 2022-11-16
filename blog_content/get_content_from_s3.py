from pathlib import Path
import os
import environ
import boto3


def get_s3_bucket_name() -> str:
    env = environ.Env()
    env.read_env(os.path.join(Path(__file__).resolve().parent.parent, 'env'))
    return env('AWS_STORAGE_BUCKET_NAME')


def get_content(blog_title_name: str) -> str:
    s3_client = boto3.client('s3')
    s3_object = s3_client.get_object(
        Bucket=get_s3_bucket_name(), Key='blog_content/{}.txt'.format(blog_title_name)
    )
    return s3_object['Body'].read()