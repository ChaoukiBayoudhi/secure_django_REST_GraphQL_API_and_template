from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class UserRole(models.TextChoices):
    AUTHOR = 'Author', 'Author'
    REVIEWER = 'Reviewer', 'Reviewer'
    EDITOR = 'Editor', 'Editor'
    ADMIN = 'Admin', 'Admin'

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
        
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', UserRole.ADMIN)
        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=UserRole.choices)
    
    username = None  # Remove default username field
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'role']
    
    objects = UserManager()
    
    def __str__(self):
        return self.email

    class Meta:
        db_table = 'users'
        ordering = ['email']