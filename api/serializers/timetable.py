from rest_framework import serializers
from bioattend.models import Timetable


class TimetableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timetable
        fields = '__all__'


class StudentTimetableInputSerializer(serializers.Serializer):
    studentID = serializers.IntegerField(required=True)
    day = serializers.CharField(max_length=10, required=True)


class LecturerTimetableInputSerializer(serializers.Serializer):
    lecturerID = serializers.IntegerField(required=True)
    day = serializers.CharField(max_length=10, required=True)
