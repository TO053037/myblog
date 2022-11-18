from django.shortcuts import render
from blog_content import get_content_from_s3
from django.views.generic.list import ListView
from .models import Article


class IndexView(ListView):
    model = Article
    paginate_by = 50
    template_name = 'blogapp/index.html'
    context_object_name = 'articles'
