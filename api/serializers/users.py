from django.contrib.auth import authenticate
from rest_framework import serializers
from users.models import User
from django.contrib.auth.models import update_last_login
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from bioattend.models import Student, Lecturer

class UserSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField()
    id = serializers.UUIDField(source='public_id', read_only=True)
    image = serializers.ImageField(required=False)  # Add image field

    class Meta:
        model = User
        fields = ['id', 'user_name', 'email', 'number', 'role', 'image']

    def get_role(self, obj):
        if Student.objects.filter(user=obj).exists():
            return 'student'
        elif Lecturer.objects.filter(user=obj).exists():
            return 'teacher'
        return 'unknown'

class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        user = UserSerializer(self.user).data
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['user'] = user

        update_last_login(None, self.user)

        return data
