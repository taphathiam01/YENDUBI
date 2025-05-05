
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('client', 'Client'),
        ('gerant', 'Gérant'),
    )

    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='client')

    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'phone_number']
    USERNAME_FIELD = 'username'

    def __str__(self):
        return f"{self.username} ({self.role})"
