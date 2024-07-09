from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
import uuid
from .managers import CustomUserManager
# Create your models here.
class User(AbstractBaseUser,PermissionsMixin):
    public_id = models.UUIDField(db_index=True, unique=True, editable=False, default=uuid.uuid4)
    user_name = models.CharField(max_length=90)
    email = models.EmailField(db_index=True, unique=True)
    number = models.CharField(max_length=9)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)


    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ["user_name", "number"]

    objects = CustomUserManager()