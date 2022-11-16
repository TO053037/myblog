from django.shortcuts import render
import boto3


def index(request):
    import environ
    from pathlib import Path
    env = environ.Env()
    import os
    BASE_DIR = Path(__file__).resolve().parent.parent
    env.read_env(os.path.join(BASE_DIR, '.env'))

    s3_client = boto3.client('s3')
    s3_object = s3_client.get_object(
        Bucket=env('AWS_STORAGE_BUCKET_NAME'), Key='blog_content/test記事.txt'
    )
    print(s3_object['Body'].read())
    return render(request, 'blogapp/index.html')
