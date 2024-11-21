from django.db import models
from django.contrib.auth.models import AbstractUser

from .service import CustomManager

class User(AbstractUser):
    last_login = None
    username = None

    email = models.EmailField(unique=True)
    icon = models.ImageField(upload_to='users_icons', null=True, blank=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomManager()

    def save(self, *args, **kwargs):
        if self.is_staff:
            self.is_active = True
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"Email: {self.email}"
    
