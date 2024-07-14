from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
import uuid

from .managers import CustomUserManager

class User(AbstractBaseUser, PermissionsMixin):
    public_id = models.UUIDField(db_index=True, unique=True, editable=False, default=uuid.uuid4)
    user_name = models.CharField(max_length=90, unique = True )
    email = models.EmailField(db_index=True, unique=True)
    number = models.CharField(max_length=15)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = ['email', 'number']

    def __str__(self):
        return self.email
