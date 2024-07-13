from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from bioattend.models import Student, Lecturer

class Command(BaseCommand):
    help = 'Hashes passwords of existing Student and Lecturer entries'

    def handle(self, *args, **kwargs):
        students = Student.objects.all()
        lecturers = Lecturer.objects.all()

        for student in students:
            if not student.password.startswith('pbkdf2_sha256$'):
                student.password = make_password(student.password)
                student.save()

        for lecturer in lecturers:
            if not lecturer.password.startswith('pbkdf2_sha256$'):
                lecturer.password = make_password(lecturer.password)
                lecturer.save()

        self.stdout.write(self.style.SUCCESS('Successfully hashed passwords for all existing entries'))
