import random

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class VerificationCode(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='verification_code')
    code = models.CharField(max_length=6)
    is_used = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def generate_code(self):
        self.code = f"{random.randint(100000, 999999)}"
        self.save()
