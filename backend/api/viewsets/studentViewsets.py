from rest_framework import viewsets
from api.serializers.student import StudentSerializer
from bioattend.models import Student


class StudentListViewset(viewsets.ModelViewSet):
    http_method_names = ['get', 'post']

    serializer_class = StudentSerializer

    queryset = Student.objects.all()


class StudentListViewset(viewsets.ModelViewSet):
    http_method_names = ['get', 'post']
    serializer_class = StudentSerializer

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