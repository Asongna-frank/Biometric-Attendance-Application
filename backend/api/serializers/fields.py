# api/serializers/fields.py
from rest_framework import serializers

class BinaryField(serializers.Field):
    def to_representation(self, value):
        # Convert binary data to a base64 string for representation
        return value.decode('utf-8')

    def to_internal_value(self, data):
        # Convert the base64 string back to binary data
        return data.encode('utf-8')
