from django.db import models
import datetime


class Article(models.Model):
    title = models.CharField(max_length=30)
    num_read = models.IntegerField(default=0)
    created = models.DateField(default=datetime.date.today)
    is_public = models.BooleanField(default=False)
