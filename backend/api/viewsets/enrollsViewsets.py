from rest_framework import viewsets
from rest_framework.response import Response
from bioattend.models import Enrolls
from api.serializers.enrolls import EnrollsSerializer


class EnrollsListViewset(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'delete']
    serializer_class = EnrollsSerializer
    queryset = Enrolls.objects.all()

    def get_queryset(self):
        queryset = Enrolls.objects.all()

        student_id = self.request.query_params.get('studentID', None)
        course_id = self.request.query_params.get('courseID', None)

        if student_id is not None:
            queryset = queryset.filter(studentID__userID=student_id)
        if course_id is not None:
            queryset = queryset.filter(courseID__courseID=course_id)

        return queryset
