from rest_framework import viewsets, status
from rest_framework.response import Response
from api.serializers.lecturer import LecturerSerializer
from bioattend.models import Lecturer


class LecturerListViewset(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    serializer_class = LecturerSerializer

    queryset = Lecturer.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        lecturer_name = self.request.query_params.get('lecturerName', None)
        if lecturer_name:
            queryset = queryset.filter(lecturerName__icontains=lecturer_name)
        return queryset
