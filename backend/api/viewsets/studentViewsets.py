from rest_framework import viewsets
from api.serializers.student import StudentSerializer
from bioattend.models import Student

class StudentListViewset(viewsets.ModelViewSet):
    http_method_names = ['get','post']

    serializer_class = StudentSerializer

    queryset = Student.objects.all()