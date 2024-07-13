# admin.py
from django.contrib import admin
from django.shortcuts import render
from django.urls import path
from django.http import HttpResponseRedirect
import csv, json, pandas as pd
from .forms import UploadFileForm
from .models import *


def upload_file(modeladmin, request, queryset):
    if 'apply' in request.POST:
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            data_frame = None

            if file.name.endswith('.csv'):
                data_frame = pd.read_csv(file)
            elif file.name.endswith('.xlsx'):
                data_frame = pd.read_excel(file)
            elif file.name.endswith('.json'):
                data_frame = pd.read_json(file)

            if data_frame is not None:
                model_class = modeladmin.model
                for _, row in data_frame.iterrows():
                    obj = model_class(**row.to_dict())
                    obj.save()
                modeladmin.message_user(request, "Data uploaded successfully!")
                return HttpResponseRedirect(request.get_full_path())

    form = UploadFileForm()
    return render(request, 'admin/upload_file.html', {'form': form})


upload_file.short_description = "Upload CSV/Excel/JSON file to this table"


class StudentAdmin(admin.ModelAdmin):
    list_display = ["userID", "matricule", "studentName", "email", "password", "department", "level"]
    search_fields = ["matricule", "studentName", "department", "level"]
    list_filter = ["department", "level"]
    actions = [upload_file]


class LecturerAdmin(admin.ModelAdmin):
    list_display = ["userID", "lecturerName", "number", "email", "password"]
    search_fields = ["lecturerName", "number", "email"]
    actions = [upload_file]


class CourseAdmin(admin.ModelAdmin):
    list_display = ["courseID", "courseName", "courseCode", "semester"]
    search_fields = ["courseName", "courseCode", "semester"]
    list_filter = ["semester"]
    actions = [upload_file]


class TeachesAdmin(admin.ModelAdmin):
    list_display = ["lecturerID", "courseID"]
    search_fields = ["lecturerID", "courseID"]
    list_filter = ["courseID"]
    actions = [upload_file]


class AttendanceAdmin(admin.ModelAdmin):
    list_display = ["recordID", "student", "course", "date", "status"]
    search_fields = ["student", "course", "date", "status"]
    list_filter = ["course", "status"]
    actions = [upload_file]


class EnrollsAdmin(admin.ModelAdmin):
    list_display = ["studentID", "courseID"]
    search_fields = ["studentID", "courseID"]
    list_filter = ["courseID"]
    actions = [upload_file]


class TimetableAdmin(admin.ModelAdmin):
    list_display = ["timetableID", "course", "lecturer", "day", "start_time", "end_time", "room"]
    search_fields = ["course", "lecturer", "day", "start_time", "end_time", "room"]
    list_filter = ["day", "course", "room", "start_time", "end_time"]
    actions = [upload_file]


class FingerprintAdmin(admin.ModelAdmin):
    list_display = ["student", "fingerprint_data"]
    search_fields = ["student"]
    list_filter = ["student"]
    actions = [upload_file]


admin.site.register(Student, StudentAdmin)
admin.site.register(Lecturer, LecturerAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Teaches, TeachesAdmin)
admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(Enrolls, EnrollsAdmin)
admin.site.register(Timetable, TimetableAdmin)
admin.site.register(Fingerprint, FingerprintAdmin)
