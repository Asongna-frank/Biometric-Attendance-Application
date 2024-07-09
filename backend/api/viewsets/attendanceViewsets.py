from rest_framework import viewsets, status
from rest_framework.response import Response
from api.serializers.attendance import AttendanceSerializer
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
