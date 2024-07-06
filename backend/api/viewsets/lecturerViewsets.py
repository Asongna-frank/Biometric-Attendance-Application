from rest_framework import viewsets
from api.serializers.lecturer import LecturerSerializer
from bioattend.models import Lecturer


class LecturerListViewset(viewsets.ModelViewSet):
    http_method_names = ['get', 'post']

    serializer_class = LecturerSerializer

    queryset = Lecturer.objects.all()


class LecturerListViewset(viewsets.ModelViewSet):
    http_method_names = ['get', 'post']
    serializer_class = LecturerSerializer
    queryset = Lecturer.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        lecturer_name = self.request.query_params.get('lecturerName', None)
        if lecturer_name:
            queryset = queryset.filter(lecturerName__icontains=lecturer_name)
        return queryset