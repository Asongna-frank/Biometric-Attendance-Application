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

    def get_user_name(self, obj):
        return obj.user.user_name
    get_user_name.short_description = 'User Name'

@admin.register(Lecturer, site=custom_admin_site)
class LecturerAdmin(admin.ModelAdmin):
    form = LecturerForm
    list_display = ['get_user_name', 'lecturerID']
    search_fields = ['user__email', 'user__user_name', 'lecturerID']

    def get_user_name(self, obj):
        return obj.user.user_name
    get_user_name.short_description = 'User Name'

@admin.register(Administrator, site=custom_admin_site)
class AdministratorAdmin(admin.ModelAdmin):
    form = AdministratorForm
    list_display = ['get_user_name', 'administratorID']
    search_fields = ['user__email', 'user__user_name', 'administratorID']

    def get_user_name(self, obj):
        return obj.user.user_name
    get_user_name.short_description = 'User Name'


@admin.register(Course, site=custom_admin_site)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('courseCode', 'courseName', 'get_course_description')

    def get_course_description(self, obj):
        return obj.courseDescription
    get_course_description.short_description = 'Course Description'

@admin.register(Attendance, site=custom_admin_site)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'date', 'status')

@admin.register(Timetable, site=custom_admin_site)
class TimetableAdmin(admin.ModelAdmin):
    list_display = ('course', 'lecturer', 'day', 'start_time', 'end_time', 'room')
