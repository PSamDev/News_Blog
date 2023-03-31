from django.contrib import admin
from . models import Category, News, Comment, Message

# Register your models here.
admin.site.register(Category)

class AdminNews(admin.ModelAdmin):
    list_display = ("title", "category", "post_time")
    
admin.site.register(News, AdminNews)

class AdminComment(admin.ModelAdmin):
    list_display = ("name", "news", "comment", "comment_time", "status")
    
admin.site.register(Comment, AdminComment)

class AdminMessage(admin.ModelAdmin):
    list_display = ("name","message")

admin.site.register(Message, AdminMessage)
