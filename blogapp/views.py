from django.shortcuts import render
from blog_content import get_content_from_s3


def index(request):
    print(get_content_from_s3.get_content('test記事'))
    return render(request, 'blogapp/index.html')
