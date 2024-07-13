# api/serializers/fingerprint.py
from rest_framework import serializers
from bioattend.models import Fingerprint
from .fields import BinaryField

class FingerprintSerializer(serializers.ModelSerializer):
    fingerprint_data = BinaryField()

    class Meta:
        model = Fingerprint
        fields = '__all__'
