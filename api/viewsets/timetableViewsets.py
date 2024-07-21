from django.utils.dateparse import parse_date
from datetime import time
from rest_framework import viewsets, status
from api.serializers.timetable import TimetableSerializer
from bioattend.models import Timetable


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


# class TimetableViewset(viewsets.ModelViewSet):
#     http_method_names = ['get', 'post', 'put', 'patch', 'delete']
#     serializer_class = TimetableSerializer
#     queryset = Timetable.objects.all()
#
#     def get_queryset(self):
#         queryset = Timetable.objects.all()
#
#         course_id = self.request.query_params.get('course', None)
#         lecturer_id = self.request.query_params.get('lecturer', None)
#         day = self.request.query_params.get('day', None)
#         start_time = self.request.query_params.get('start_time', None)
#         end_time = self.request.query_params.get('end_time', None)
#         room = self.request.query_params.get('room', None)
#
#         if course_id is not None:
#             queryset = queryset.filter(course__id=course_id)
#         if lecturer_id is not None:
#             queryset = queryset.filter(lecturer__id=lecturer_id)
#         if day is not None:
#             queryset = queryset.filter(day__icontains=day)
#         if start_time is not None:
#             parsed_start_time = parse_date(start_time)
#             if parsed_start_time:
#                 queryset = queryset.filter(start_time__gte=time.fromisoformat(start_time))
#         if end_time is not None:
#             parsed_end_time = parse_date(end_time)
#             if parsed_end_time:
#                 queryset = queryset.filter(end_time__lte=time.fromisoformat(end_time))
#         if room is not None:
#             queryset = queryset.filter(room__icontains=room)
#
#         return queryset
