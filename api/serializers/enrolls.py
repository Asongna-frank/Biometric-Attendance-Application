from rest_framework import serializers
from bioattend.models import Enrolls


class EnrollsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrolls
        fields = '__all__'