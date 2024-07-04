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
    fullName = models.CharField(max_length=70)
    #    role = models.CharField(max_length=13, choices=ROLE_CHOICES)
    email = models.EmailField(max_length=90)
    password = models.CharField(max_length=20)
    #    biometricData = models.BinaryField()
    department = models.CharField(max_length=50, choices=department_choices)
    level = models.CharField(max_length=10, choices=level_choices)

    def __str__(self):
        return self.matricule
