from django.contrib import admin
from .models import Post
from django.db import models
from tinymce import TinyMCE

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')

    formfield_overrides = {
        models.TextField: {"widget": TinyMCE()}
        }

admin.site.register(Post, PostAdmin)
