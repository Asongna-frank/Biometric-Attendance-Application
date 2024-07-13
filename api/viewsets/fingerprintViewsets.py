# api/views/fingerprint.py
from rest_framework import viewsets
from rest_framework.response import Response
from bioattend.models import Fingerprint
from api.serializers.fingerprint import FingerprintSerializer

class FingerprintViewset(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'delete']
    serializer_class = FingerprintSerializer
    queryset = Fingerprint.objects.all()

    def get_queryset(self):
        queryset = Fingerprint.objects.all()
        student_id = self.request.query_params.get('studentID', None)

        if student_id is not None:
            queryset = queryset.filter(student__userID=student_id)

        return queryset
