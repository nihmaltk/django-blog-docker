"""
Admin interface configuration for User model.
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """
    Custom admin interface for User model.
    Extends Django's default UserAdmin to include our custom fields.
    """
    
    list_display = [
        'username',
        'email',
        'first_name',
        'last_name',
        'is_staff',
        'is_active',
        'date_joined',
        'post_count'
    ]
    
    list_filter = [
        'is_staff',
        'is_active',
        'is_superuser',
        'date_joined',
    ]
    
    search_fields = ['username', 'email', 'first_name', 'last_name']
    
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Additional Info', {
            'fields': ('bio', 'avatar', 'website', 'location')
        }),
    )
    
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('Additional Info', {
            'fields': ('email', 'bio', 'avatar', 'website', 'location')
        }),
    )
    
    def post_count(self, obj):
        """Display number of posts by user."""
        return obj.post_count
    post_count.short_description = 'Posts'
