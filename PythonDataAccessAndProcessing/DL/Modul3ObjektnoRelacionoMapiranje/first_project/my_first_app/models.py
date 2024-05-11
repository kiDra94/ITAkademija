from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

class Car(models.Model):
    brend = models.CharField(max_length=45)
    student = models.OneToOneField(#oznacva da 1 stud ima 1 car
        Student,
        on_delete=models.CASCADE,
        related_name='car'
    )

