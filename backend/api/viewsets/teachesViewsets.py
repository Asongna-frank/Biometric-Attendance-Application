from rest_framework import viewsets
from rest_framework.response import Response
from bioattend.models import Teaches
from api.serializers.teaches import TeachesSerializer


class TeachesListViewset(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'delete']
    serializer_class = TeachesSerializer
    queryset = Teaches.objects.all()

    def delete(self, request, pk=None):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_queryset(self):
        queryset = Teaches.objects.all()

        instructor_id = self.request.query_params.get('instructorID', None)
        course_id = self.request.query_params.get('courseID', None)

        if instructor_id is not None:
            queryset = queryset.filter(instructorID__userID=instructor_id)
        if course_id is not None:
            queryset = queryset.filter(courseID__courseID=course_id)

        return queryset
