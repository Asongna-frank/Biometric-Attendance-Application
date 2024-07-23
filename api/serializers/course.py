from rest_framework import serializers
from bioattend.models import Course, Lecturer


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class LecturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecturer
        fields = ['lecturerID', 'user']

class LecturerDetailSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.user_name')
    email = serializers.EmailField(source='user.email')
    number = serializers.CharField(source='user.number')
    image = serializers.ImageField(source='user.image')

    class Meta:
        model = Lecturer
        fields = ['lecturerID', 'user_name', 'email', 'number', 'image']