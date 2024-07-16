from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.forms import ValidationError

class CustomUserManager(BaseUserManager):

    def get_object_by_public_id(self, public_id):
        try:
            instance = self.get(public_id=public_id)
            return instance
        except ObjectDoesNotExist:
            raise Http404("Object does not exist")
        except (ValueError, TypeError, ValidationError):
            raise Http404("Invalid public_id")

    def create_user(self, user_name, email, number, password=None, **extra_fields):
        if user_name is None:
            raise ValueError("User Name is required")
        if email is None:
            raise ValueError("Email is required")
        if number is None:
            raise ValueError("Number is required")

        email = self.normalize_email(email)
        user = self.model(user_name=user_name, email=email, number=number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_name, email, number, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        return self.create_user(user_name=user_name, email=email, number=number, password=password, **extra_fields)
