from rest_framework import viewsets, status
from rest_framework.response import Response
from api.serializers.lecturer import LecturerSerializer
from bioattend.models import Lecturer


class LecturerListViewset(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    serializer_class = LecturerSerializer

    queryset = Lecturer.objects.all()

    def put(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def patch(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=None):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_queryset(self):
        queryset = self.queryset
        lecturer_name = self.request.query_params.get('lecturerName', None)
        if lecturer_name:
            queryset = queryset.filter(lecturerName__icontains=lecturer_name)
        return queryset
