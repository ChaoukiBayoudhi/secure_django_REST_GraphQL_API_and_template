from django.db import models
from django.contrib.auth.models import AbstractUser

class UserRole(models.TextChoices):
    AUTHOR = 'Author', 'Author'
    REVIEWER = 'Reviewer', 'Reviewer'
    EDITOR = 'Editor', 'Editor'
    ADMIN = 'Admin', 'Admin'

class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    role = models.CharField(max_length=20, choices=UserRole.choices, null=True)
    
    username = None  # Remove default username field
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Removes email from required fields (it's now the USERNAME_FIELD)

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'users'
        ordering = ['email']