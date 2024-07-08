from django.contrib import admin

from .models import Student, Lecturer, Course, Teaches, Attendance, Enrolls
# admin.site.register(Student)
# admin.site.register(Lecturer)
# admin.site.register(Course)
# admin.site.register(Teaches)
# admin.site.register(Attendance)
# admin.site.register(Enrolls)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["userID", "matricule", "studentName", "email", "password", "department", "level"]

    search_fields = ["userID", "matricule", "studentName", "department", "level"]

    list_filter = ["department", "level"]