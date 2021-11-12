from django.contrib import admin

# Register your models here.
from .models import Post, Vote


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "views", "rating")
    list_display_links = ("id", "title")


admin.site.register(Vote)
