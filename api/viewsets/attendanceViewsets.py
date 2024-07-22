from rest_framework import viewsets, status
from api.serializers.attendance import AttendanceSerializer, StudentAttendanceInputSerializer, \
    LecturerAttendanceInputSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from api.serializers.timetable import StudentTimetableInputSerializer
from bioattend.models import Attendance
from django.utils.dateparse import parse_date

class AttendanceListViewset(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    serializer_class = AttendanceSerializer
    queryset = Attendance.objects.all()

    def get_queryset(self):
        queryset = Attendance.objects.all()

        student_id = self.request.query_params.get('student', None)
        course_id = self.request.query_params.get('course', None)
        date = self.request.query_params.get('date', None)
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)
        status = self.request.query_params.get('status', None)

        if student_id is not None:
            queryset = queryset.filter(student__id=student_id)
        if course_id is not None:
            queryset = queryset.filter(course__id=course_id)
        if date is not None:
            parsed_date = parse_date(date)
            if parsed_date:
                queryset = queryset.filter(date__date=parsed_date)
        if start_date is not None and end_date is not None:
            parsed_start_date = parse_date(start_date)
            parsed_end_date = parse_date(end_date)
            if parsed_start_date and parsed_end_date:
                queryset = queryset.filter(date__date__range=(parsed_start_date, parsed_end_date))
        elif start_date is not None:
            parsed_start_date = parse_date(start_date)
            if parsed_start_date:
                queryset = queryset.filter(date__date__gte=parsed_start_date)
        elif end_date is not None:
            parsed_end_date = parse_date(end_date)
            if parsed_end_date:
                queryset = queryset.filter(date__date__lte=parsed_end_date)
        if status is not None:
            queryset = queryset.filter(status__icontains=status)

        return queryset


class StudentAttendanceView(viewsets.ViewSet):
    @action(detail=False, methods=['post'])
    def get_student_attendance(self, request):
        serializer = StudentAttendanceInputSerializer(data=request.data)
        if serializer.is_valid():
            student_id = serializer.validated_data['studentID']

            attendance_records = Attendance.objects.filter(student__id=student_id)
            attendance_serializer = AttendanceSerializer(attendance_records, many=True)

            return Response(attendance_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LecturerAttendanceView(viewsets.ViewSet):
    @action(detail=False, methods=['post'])
    def get_lecturer_attendance(self, request):
        serializer = LecturerAttendanceInputSerializer(data=request.data)
        if serializer.is_valid():
            course_ids = serializer.validated_data['courseIDs']

            attendance_records = Attendance.objects.filter(course_id__in=course_ids)
            attendance_serializer = AttendanceSerializer(attendance_records, many=True)

            return Response(attendance_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)