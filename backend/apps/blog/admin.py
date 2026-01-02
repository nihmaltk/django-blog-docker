"""
Admin interface configuration for blog models.
"""

from django.contrib import admin
from .models import Category, Tag, Post, Comment

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'author',
        'category',
        'status',
        'views',
        'published_at',
        'comment_count'
    ]
    list_filter = ['status', 'category', 'created_at', 'published_at']
    search_fields = ['title', 'content', 'author__username']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_at'
    
    fieldsets = (
        ('Content', {
            'fields': ('title', 'slug', 'content', 'excerpt', 'featured_image')
        }),
        ('Relationships', {
            'fields': ('author', 'category', 'tags')
        }),
        ('Publication', {
            'fields': ('status', 'published_at')
        }),
        ('Metadata', {
            'fields': ('views',),
            'classes': ('collapse',)
        }),
    )
    
    filter_horizontal = ['tags']
    
    def comment_count(self, obj):
        return obj.comment_count
    comment_count.short_description = 'Comments'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        'author',
        'post',
        'content_preview',
        'approved',
        'is_reply',
        'created_at'
    ]
    list_filter = ['approved', 'created_at']
    search_fields = ['author__username', 'post__title', 'content']
    
    def content_preview(self, obj):
        """Show first 50 characters of comment."""
        return obj.content[:50] + '...' if len(obj.content) > 50 else obj.content
    content_preview.short_description = 'Content'
    
    def is_reply(self, obj):
        """Show if comment is a reply."""
        return '✓' if obj.is_reply else '✗'
    is_reply.short_description = 'Reply'
