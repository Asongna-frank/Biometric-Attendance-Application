from rest_framework import serializers
from bioattend.models import Attendance, Student, Lecturer
from rest_framework import serializers


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'



class StudentAttendanceInputSerializer(serializers.Serializer):
    studentID = serializers.IntegerField(required=True)

class LecturerAttendanceInputSerializer(serializers.Serializer):
    courseIDs = serializers.ListField(
        child=serializers.IntegerField(),
        required=True
    )

class LecturerDetailSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.user_name')
    email = serializers.EmailField(source='user.email')
    number = serializers.CharField(source='user.number')
    image = serializers.ImageField(source='user.image')

    class Meta:
        model = Lecturer
        fields = ['lecturerID', 'user_name', 'email', 'number', 'image']

class StudentSerializerAttendance(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.user_name')
    image = serializers.ImageField(source='user.image')

    class Meta:
        model = Student
        fields = ['id', 'user_name', 'image']

class AttendanceSerializer1(serializers.ModelSerializer):
    student_name = serializers.CharField(source='student.user.user_name')
    student_image = serializers.ImageField(source='student.user.image')

    class Meta:
        model = Attendance
        fields = ['recordID', 'date', 'status', 'student', 'course', 'student_name', 'student_image']
