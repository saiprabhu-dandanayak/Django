# Inside populate_db.py

from django.core.management.base import BaseCommand
from testapp.models import Student
from faker import Faker
from random import randint

fake = Faker()

def phonenumbergen():
    d1 = randint(6, 9)
    num = str(d1)
    for i in range(9):
        num += str(randint(0, 9))
    return int(num)

class Command(BaseCommand):
    help = 'Populate the database with fake student records'

    def handle(self, *args, **kwargs):
        for i in range(30):
            frollno = fake.random_int(min=1, max=999)
            fname = fake.name()
            fdob = fake.date()
            fmarks = fake.random_int(min=1, max=100)
            femail = fake.email()
            fphonenumber = phonenumbergen()
            faddress = fake.address()
            student_record = Student.objects.get_or_create(
                rollno=frollno,
                name=fname,
                dob=fdob,
                marks=fmarks,
                email=femail,
                phonenumber=fphonenumber,
                address=faddress
            )
