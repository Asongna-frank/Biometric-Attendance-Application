from rest_framework import serializers
from bioattend.models import Lecturer

class LecturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecturer
        fields = '__all__'
