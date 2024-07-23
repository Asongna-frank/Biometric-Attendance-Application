from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from bioattend.models import Course, Lecturer, Teaches
from api.serializers.classroster import CourseWithStudentsSerializer

class ClassRosterView(viewsets.ViewSet):
    http_method_names = ['post']

    @action(detail=False, methods=['post'])
    def get_class_roster(self, request):
        lecturer_id = request.data.get('lecturerID')
        if not lecturer_id:
            return Response({'error': 'Lecturer ID is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            lecturer = Lecturer.objects.get(lecturerID=lecturer_id)
        except Lecturer.DoesNotExist:
            return Response({'error': 'Lecturer not found'}, status=status.HTTP_404_NOT_FOUND)

        teaches = Teaches.objects.filter(lecturerID=lecturer)
        courses = [teach.courseID for teach in teaches]
        courses_with_students = CourseWithStudentsSerializer(courses, many=True).data

        return Response(courses_with_students, status=status.HTTP_200_OK)
