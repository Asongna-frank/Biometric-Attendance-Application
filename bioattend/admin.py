from django.contrib import admin
from .models import Student, Lecturer, Course, Teaches, Attendance, Enrolls, Timetable


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["userID", "matricule", "studentName", "email", "password", "department", "level"]
    search_fields = ["matricule", "studentName", "department", "level"]
    list_filter = ["department", "level"]


@admin.register(Lecturer)
class LecturerAdmin(admin.ModelAdmin):
    list_display = ["userID", "lecturerName", "number", "email", "password"]
    search_fields = ["lecturerName", "number", "email"]

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["courseID", "courseName", "courseCode", "semester"]
    search_fields = ["courseName", "courseCode", "semester"]
    list_filter = ["semester"]


@admin.register(Teaches)
class TeachesAdmin(admin.ModelAdmin):
    list_display = ["lecturerID", "courseID"]
    search_fields = ["lecturerID", "courseID"]
    list_filter = ["courseID"]


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ["recordID", "student", "course", "date", "status"]
    search_fields = ["student", "course", "date", "status"]
    list_filter = ["course", "status"]


@admin.register(Enrolls)
class EnrollsAdmin(admin.ModelAdmin):
    list_display = ["studentID", "courseID"]
    search_fields = ["studentID", "courseID"]
    list_filter = ["courseID"]


@admin.register(Timetable)
class TimetableAdmin(admin.ModelAdmin):
    list_display = ["timetableID", "course", "lecturer", "day", "start_time", "end_time", "room"]
    search_fields = ["course", "lecturer", "day", "start_time", "end_time", "room"]
    list_filter = ["day", "course", "room", "start_time", "end_time"]