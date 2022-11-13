from django.contrib import admin
from blogapp.models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'num_read', 'is_public')


admin.site.register(Article, ArticleAdmin)
