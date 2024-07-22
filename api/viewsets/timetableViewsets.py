from django.utils.dateparse import parse_date
from rest_framework import viewsets, status
from rest_framework.response import Response
from datetime import time
from rest_framework.decorators import action
from api.serializers.timetable import TimetableSerializer
from api.serializers.course import CourseSerializer
from api.serializers.timetable import StudentTimetableInputSerializer, LecturerTimetableInputSerializer
from bioattend.models import Timetable, Enrolls, Teaches, Course


class TimetableViewset(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    serializer_class = TimetableSerializer
    queryset = Timetable.objects.all()

    def get_queryset(self):
        queryset = Timetable.objects.all()

        course_id = self.request.query_params.get('course', None)
        lecturer_id = self.request.query_params.get('lecturer', None)
        day = self.request.query_params.get('day', None)
        start_time = self.request.query_params.get('start_time', None)
        end_time = self.request.query_params.get('end_time', None)
        room = self.request.query_params.get('room', None)

        if course_id is not None:
            queryset = queryset.filter(course__id=course_id)
        if lecturer_id is not None:
            queryset = queryset.filter(lecturer__id=lecturer_id)
        if day is not None:
            queryset = queryset.filter(day__icontains=day)
        if start_time is not None:
            parsed_start_time = parse_date(start_time)
            if parsed_start_time:
                queryset = queryset.filter(start_time__gte=time.fromisoformat(start_time))
        if end_time is not None:
            parsed_end_time = parse_date(end_time)
            if parsed_end_time:
                queryset = queryset.filter(end_time__lte=time.fromisoformat(end_time))
        if room is not None:
            queryset = queryset.filter(room__icontains=room)

        return queryset


class StudentTimetableView(viewsets.ViewSet):
    @action(detail=False, methods=['post'])
    def get_student_timetable(self, request):
        serializer = StudentTimetableInputSerializer(data=request.data)
        if serializer.is_valid():
            student_id = serializer.validated_data['studentID']
            day = serializer.validated_data['day']

            enrolls = Enrolls.objects.filter(studentID=student_id).values_list('courseID', flat=True)
            courses = Course.objects.filter(courseID__in=enrolls)
            timetable = Timetable.objects.filter(course__in=courses, day=day)

            course_serializer = CourseSerializer(courses, many=True)
            timetable_serializer = TimetableSerializer(timetable, many=True)

            return Response({
                'courses': course_serializer.data,
                'timetable': timetable_serializer.data
            }, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LecturerTimetableView(viewsets.ViewSet):
    @action(detail=False, methods=['post'])
    def get_lecturer_timetable(self, request):
        serializer = LecturerTimetableInputSerializer(data=request.data)
        if serializer.is_valid():
            lecturer_id = serializer.validated_data['lecturerID']
            day = serializer.validated_data['day']

            teaches = Teaches.objects.filter(lecturerID=lecturer_id).values_list('courseID', flat=True)
            courses = Course.objects.filter(courseID__in=teaches)
            timetable = Timetable.objects.filter(course__in=courses, day=day)

            course_serializer = CourseSerializer(courses, many=True)
            timetable_serializer = TimetableSerializer(timetable, many=True)

            return Response({
                'courses': course_serializer.data,
                'timetable': timetable_serializer.data
            }, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
