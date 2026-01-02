"""
Custom User model for authentication.
Extends Django's AbstractUser to allow future customization.
"""

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """
    Custom User model.
    
    Inherits from AbstractUser which provides:
    - username, email, password (hashed)
    - first_name, last_name
    - is_staff, is_active, is_superuser
    - date_joined, last_login
    
    We extend it to add custom fields.
    """
    
    bio = models.TextField(
        max_length=500,
        blank=True,
        help_text="Short biography of the user"
    )
    
    avatar = models.ImageField(
        upload_to='avatars/',
        blank=True,
        null=True,
        help_text="User profile picture"
    )
    
    website = models.URLField(
        max_length=200,
        blank=True,
        help_text="Personal website or blog"
    )
    
    location = models.CharField(
        max_length=100,
        blank=True,
        help_text="City, Country"
    )
    
    email = models.EmailField(
        unique=True,
        help_text="Email address (must be unique)"
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['-date_joined'] 
    
    def __str__(self):
        """String representation of user."""
        return self.username
    
    def get_full_name(self):
        """Return user's full name or username if name not set."""
        full_name = super().get_full_name()
        return full_name if full_name else self.username
    
    @property
    def post_count(self):
        """Return number of blog posts by this user."""
        return self.blog_posts.count()
