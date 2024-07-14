from django.db import models
from users.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department_choices = [
        ('computer', 'Computer Engineering'),
        ('electrical', 'Electrical Engineering'),
        ('mechanical', 'Mechanical Engineering'),
        ('civil', 'Civil Engineering'),
    ]
    level_choices = [
        ('200', 'Level 200'),
        ('300', 'Level 300'),
        ('400', 'Level 400'),
        ('500', 'Level 500'),
        ('550', 'Level 550'),
    ]
    matricule = models.CharField(max_length=9, unique=True)
    department = models.CharField(max_length=50, choices=department_choices)
    level = models.CharField(max_length=10, choices=level_choices)

    class Meta:
        ordering = ["user__user_name", "department", "level"]

    def __str__(self):
        return f'{self.user.user_name} ({self.matricule})'

class Administrator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    administratorID = models.AutoField(primary_key=True)

    def __str__(self):
        return self.user.user_name

class Lecturer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    lecturerID = models.AutoField(primary_key=True)

    def __str__(self):
        return self.user.user_name



class Course(models.Model):
    department_choices = [
        ('computer', 'Computer Engineering'),
        ('electrical', 'Electrical Engineering'),
        ('mechanical', 'Mechanical Engineering'),
        ('civil', 'Civil Engineering'),
    ]

    semester_choices = [
        ('first', 'First Semester'),
        ('second', 'Second Semester')
    ]

    courseID = models.AutoField(primary_key=True)
    courseName = models.CharField(max_length=70)
    courseCode = models.CharField(max_length=7)
    department = models.CharField(max_length=50, choices=department_choices)
    semester = models.CharField(max_length=20, choices=semester_choices)

    class Meta:
        ordering = ["courseID", "courseName"]

    def __str__(self):
        return self.courseName


class Teaches(models.Model):
    lecturerID = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    courseID = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('lecturerID', 'courseID'),)

    def __str__(self):
        return f"{self.lecturerID} teaches {self.courseID}"


class Enrolls(models.Model):
    studentID = models.ForeignKey(Student, on_delete=models.CASCADE)
    courseID = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('studentID', 'courseID'),)

    def __str__(self):
        return f"{self.studentID} enrolled for {self.courseID}"


class Attendance(models.Model):
    status_choices = [
        ('present', 'Present'),
        ('absent', 'Absent')
    ]

    recordID = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateTimeField()
    status = models.CharField(max_length=7, choices=status_choices)

    class Meta:
        ordering = ["recordID", "student__user__user_name", "course__courseName", "date"]
        indexes = [
            models.Index(fields=["student", "course"]),
        ]

    def __str__(self):
        return f"{self.student.studentName} - {self.course.courseName}"


class Timetable(models.Model):
    day_choices = [
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
    ]

    timetableID = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    day = models.CharField(max_length=10, choices=day_choices)
    start_time = models.TimeField()
    end_time = models.TimeField()
    room = models.CharField(max_length=50)

    class Meta:
        ordering = ["day", "start_time", "course"]
        indexes = [
            models.Index(fields=["day", "course"]),
        ]

    def __str__(self):
        return f"{self.course.courseName} by {self.lecturer.lecturerName} on {self.day} from {self.start_time} to {self.end_time}"
