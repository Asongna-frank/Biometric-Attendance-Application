from rest_framework import serializers
from bioattend.models import Course, Student, Teaches, Enrolls

class StudentInCourseSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.user_name')
    email = serializers.EmailField(source='user.email')
    number = serializers.CharField(source='user.number')
    image = serializers.ImageField(source='user.image')

    class Meta:
        model = Student
        fields = ['id', 'user_name', 'email', 'number', 'image']

class CourseWithStudentsSerializer(serializers.ModelSerializer):
    students = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ['courseID', 'courseName', 'courseCode', 'department', 'semester', 'students']

    def get_students(self, obj):
        enrolls = Enrolls.objects.filter(courseID=obj)
        students = [enroll.studentID for enroll in enrolls]
        return StudentInCourseSerializer(students, many=True).data
