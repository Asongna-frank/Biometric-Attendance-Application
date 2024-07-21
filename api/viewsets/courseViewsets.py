from rest_framework import viewsets, status
from rest_framework.response import Response
from api.serializers.course import CourseSerializer
from bioattend.models import Course


class CourseListViewset(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    serializer_class = CourseSerializer

    queryset = Course.objects.all()

    def get_queryset(self):
        queryset = Course.objects.all()
        courseID = self.request.query_params.get('courseID', None)

        course_name = self.request.query_params.get('courseName', None)
        course_code = self.request.query_params.get('courseCode', None)
        semester = self.request.query_params.get('semester', None)

        if courseID is not None:
            queryset = queryset.filter(courseID__icontains=courseID)
        if course_name is not None:
            queryset = queryset.filter(courseName__icontains=course_name)
        if course_code is not None:
            queryset = queryset.filter(courseCode__icontains=course_code)
        if semester is not None:
            queryset = queryset.filter(semester__icontains=semester)

        return queryset
