from rest_framework import viewsets, status
from rest_framework.response import Response
from api.serializers.course import CourseSerializer, LecturerSerializer, LecturerDetailSerializer
from api.serializers.timetable import TimetableSerializer
from bioattend.models import Course, Timetable, Student, Lecturer, Enrolls, Teaches


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


class StudentCoursesView(viewsets.ViewSet):
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        student_id = request.data.get('studentID')
        if not student_id:
            return Response({'error': 'Student ID is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            student = Student.objects.get(id=student_id)
        except Student.DoesNotExist:
            return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

        enrollments = Enrolls.objects.filter(studentID=student)
        courses_data = []

        for enrollment in enrollments:
            course = enrollment.courseID
            course_serializer = CourseSerializer(course)
            timetables = Timetable.objects.filter(course=course)
            timetable_serializer = TimetableSerializer(timetables, many=True)

            # Get the lecturer information
            teaches = Teaches.objects.get(courseID=course)
            lecturer_serializer = LecturerDetailSerializer(teaches.lecturerID)

            courses_data.append({
                'course': course_serializer.data,
                'timetable': timetable_serializer.data,
                'lecturer': lecturer_serializer.data
            })

        return Response(courses_data, status=status.HTTP_200_OK)


class LecturerCoursesView(viewsets.ViewSet):
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        lecturer_id = request.data.get('lecturerID')
        if not lecturer_id:
            return Response({'error': 'Lecturer ID is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            lecturer = Lecturer.objects.get(lecturerID=lecturer_id)
        except Lecturer.DoesNotExist:
            return Response({'error': 'Lecturer not found'}, status=status.HTTP_404_NOT_FOUND)

        teachings = Teaches.objects.filter(lecturerID=lecturer)
        courses_data = []

        for teaching in teachings:
            course = teaching.courseID
            course_serializer = CourseSerializer(course)
            timetables = Timetable.objects.filter(course=course)
            timetable_serializer = TimetableSerializer(timetables, many=True)
            courses_data.append({
                'course': course_serializer.data,
                'timetable': timetable_serializer.data
            })

        return Response(courses_data, status=status.HTTP_200_OK)
