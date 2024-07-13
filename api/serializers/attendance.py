from rest_framework import serializers
from bioattend.models import Attendance


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'