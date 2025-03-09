from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20, unique=True)
    language = models.CharField(max_length=50)
    lesson_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    student = models.ManyToManyField(Student, related_name='teachers')
    phone_number = models.CharField(max_length=20)
    salary = models.DecimalField(max_digits=10, decimal_places=1, default=0)
    conducted_hours = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    salary = models.DecimalField(max_digits=10, decimal_places=1, default=0)
