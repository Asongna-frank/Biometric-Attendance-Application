from rest_framework import serializers
from bioattend.models import Teaches


class TeachesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teaches
        fields = '__all__'