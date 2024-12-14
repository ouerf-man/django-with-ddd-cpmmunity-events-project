from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class DjangoUser(AbstractUser):
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True, null=True)
    avatar_url = models.URLField(blank=True, null=True)

    # Override related_name to prevent clashes
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # Changed from 'user_set'
        blank=True,
        help_text='The groups this user belongs to.',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_set',  # Changed from 'user_set'
        blank=True,
        help_text='Specific permissions for this user.',
    )

    def __str__(self):
        return self.username


class Role(models.Model):
    name = models.CharField(max_length=50)
    # Add relationships if needed
