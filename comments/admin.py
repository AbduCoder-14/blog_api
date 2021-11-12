from django.contrib import admin
from mptt.admin import MPTTModelAdmin

# Register your models here.
from .models import Comment


@admin.register(Comment)
class CommentAdmin(MPTTModelAdmin, admin.ModelAdmin):
    list_display = ("id", "author", "post", "parent", "created_at")
    mptt_level_indent = 15
