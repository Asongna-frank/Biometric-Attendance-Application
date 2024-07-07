from rest_framework import viewsets, status
from rest_framework.response import Response
from api.serializers.student import StudentSerializer
from bioattend.models import Student


class StudentListViewset(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    serializer_class = StudentSerializer

    queryset = Student.objects.all()

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
        queryset = Student.objects.all()

        student_name = self.request.query_params.get('studentName', None)
        matricule = self.request.query_params.get('matricule', None)
        department = self.request.query_params.get('department', None)
        level = self.request.query_params.get('level', None)

        if student_name is not None:
            queryset = queryset.filter(studentName__icontains=student_name)
        if matricule is not None:
            queryset = queryset.filter(matricule__icontains=matricule)
        if department is not None:
            queryset = queryset.filter(department__icontains=department)
        if level is not None:
            queryset = queryset.filter(level=level)

        return queryset
