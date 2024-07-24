from django.utils.dateparse import parse_date
from rest_framework import viewsets, status
from api.serializers.attendance import AttendanceSerializer, AttendanceSerializer1, StudentAttendanceInputSerializer, StudentSerializerAttendance as StudentSerializer, LecturerAttendanceInputSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from bioattend.models import Attendance, Student, Teaches, Lecturer


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
            attendance_serializer = AttendanceSerializer1(attendance_records, many=True)

            return Response(attendance_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LecturerAttendanceView(viewsets.ViewSet):
    http_method_names = ['post']

    @action(detail=False, methods=['post'])
    def get_lecturer_attendance(self, request):
        lecturer_id = request.data.get('lecturerID')
        if not lecturer_id:
            return Response({'error': 'Lecturer ID is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            lecturer = Lecturer.objects.get(lecturerID=lecturer_id)
        except Lecturer.DoesNotExist:
            return Response({'error': 'Lecturer not found'}, status=status.HTTP_404_NOT_FOUND)

        teaches = Teaches.objects.filter(lecturerID=lecturer)
        course_ids = [teach.courseID.courseID for teach in teaches]  # Use 'courseID' if that's the field name
        attendance_records = Attendance.objects.filter(course__courseID__in=course_ids)  # Use 'courseID' if that's the field name

        data = []
        for record in attendance_records:
            record_data = AttendanceSerializer1(record).data
            student = Student.objects.get(id=record.student.id)
            student_serializer = StudentSerializer(student)
            print(f"Serialized student data: {student_serializer.data}")  # Debugging line
            record_data['student_name'] = student_serializer.data.get('user_name')
            record_data['student_image'] = student_serializer.data.get('image')
            data.append(record_data)

        return Response(data, status=status.HTTP_200_OK)
