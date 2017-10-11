from django.contrib import admin
from article.models import Article

class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title','date_time')

admin.site.register(Article,ArticleAdmin)

# Register your models here.
