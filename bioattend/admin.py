from django import forms
from django.contrib import admin
from .models import *
from users.models import User
from users.custom_admin import custom_admin_site

class StudentForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.all())

    class Meta:
        model = Student
        fields = ['user', 'matricule', 'department', 'level']

class LecturerForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.all())

    class Meta:
        model = Lecturer
        fields = ['user']

class AdministratorForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.all())

    class Meta:
        model = Administrator
        fields = ['user']

@admin.register(Student, site=custom_admin_site)
class StudentAdmin(admin.ModelAdmin):
    form = StudentForm
    list_display = ['get_user_name', 'matricule', 'department', 'level']
    search_fields = ['user__email', 'user__user_name', 'matricule', 'department', 'level']
    ordering = ['user__user_name', 'matricule', 'department', 'level']
    list_filter = ['department', 'level']

    def get_user_name(self, obj):
        return obj.user.user_name
    get_user_name.short_description = 'User Name'

@admin.register(Lecturer, site=custom_admin_site)
class LecturerAdmin(admin.ModelAdmin):
    form = LecturerForm
    list_display = ['get_user_name', 'lecturerID']
    search_fields = ['user__email', 'user__user_name', 'lecturerID']
    ordering = ['user__user_name', 'lecturerID']
    list_filter = ['lecturerID']

    def get_user_name(self, obj):
        return obj.user.user_name
    get_user_name.short_description = 'User Name'

@admin.register(Administrator, site=custom_admin_site)
class AdministratorAdmin(admin.ModelAdmin):
    form = AdministratorForm
    list_display = ['get_user_name', 'administratorID']
    search_fields = ['user__email', 'user__user_name', 'administratorID']
    ordering = ['user__user_name', 'administratorID']
    list_filter = ['administratorID']

    def get_user_name(self, obj):
        return obj.user.user_name
    get_user_name.short_description = 'User Name'

@admin.register(Course, site=custom_admin_site)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('courseCode', 'courseName', 'department', 'semester')
    search_fields = ['courseCode', 'courseName', 'department', 'semester']
    ordering = ['courseCode', 'courseName','department', 'semester']
    list_filter = ['department', 'semester']

@admin.register(Attendance, site=custom_admin_site)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'date', 'status')
    search_fields = ['student__user__user_name', 'course__courseName', 'date', 'status']
    ordering = ['date', 'student__user__user_name', 'course__courseName', 'status']
    list_filter = ['status', 'date', 'course']

@admin.register(Timetable, site=custom_admin_site)
class TimetableAdmin(admin.ModelAdmin):
    list_display = ('course', 'lecturer', 'day', 'start_time', 'end_time', 'room')
    search_fields = ['course__courseName', 'lecturer__user__user_name', 'day', 'room']
    ordering = ['day', 'start_time', 'course__courseName', 'lecturer__user__user_name']
    list_filter = ['day', 'course', 'lecturer', 'room']

@admin.register(Enrolls, site=custom_admin_site)
class EnrollsAdmin(admin.ModelAdmin):
    list_display = ('studentID', 'courseID')
    search_fields = ['studentID__user__user_name', 'courseID__courseName']
    ordering = ['studentID__user__user_name', 'courseID__courseName']
    list_filter = ['courseID']

@admin.register(Teaches, site=custom_admin_site)
class TeachesAdmin(admin.ModelAdmin):
    list_display = ('lecturerID', 'courseID')
    search_fields = ['lecturerID__user__user_name', 'courseID__courseName']
    ordering = ['lecturerID__user__user_name', 'courseID__courseName']
    list_filter = ['courseID']
