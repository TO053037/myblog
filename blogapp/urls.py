from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='blogapp/index.html'), name='index'),
    path('s3_test', views.index, name='s3_test'),
]
