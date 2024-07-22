from rest_framework import serializers
from bioattend.models import Attendance
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