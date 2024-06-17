# En tu aplicación (por ejemplo, `profiles/models.py`)
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    USER_LEVEL_CHOICES = (
        ('principiante', 'Principiante'),
        ('experimentado', 'Experimentado'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_level = models.CharField(max_length=20, choices=USER_LEVEL_CHOICES)
