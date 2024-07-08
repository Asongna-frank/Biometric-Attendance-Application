from django.db import models

class Student(models.Model):
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

    userID = models.AutoField(primary_key=True)
    matricule = models.CharField(max_length=9)
    studentName = models.CharField(max_length=70)
    email = models.EmailField(max_length=90)
    password = models.CharField(max_length=20)
    department = models.CharField(max_length=50, choices=department_choices)
    level = models.CharField(max_length=10, choices=level_choices)

    class Meta:
        ordering = ["studentName", "department", "level"]

        indexes = [
            models.Index(fields=["userID","matricule"])
        ]

    def __str__(self):
        return self.studentName


class Lecturer(models.Model):
    userID = models.AutoField(primary_key=True)
    lecturerName = models.CharField(max_length=70)
    number = models.CharField(max_length=9)
    email = models.EmailField(max_length=90)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.lecturerName


class Course(models.Model):
    semester_choices = [
        ('first', 'First Semester'),
        ('second', 'Second Semester')
    ]

    courseID = models.AutoField(primary_key=True)
    courseName = models.CharField(max_length=70)
    courseCode = models.CharField(max_length=7)
    semester = models.CharField(max_length=20, choices=semester_choices)

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

    def __str__(self):
        return f"{self.student.studentName} - {self.course.courseName}"
