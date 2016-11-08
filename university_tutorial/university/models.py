from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField()


class Course(models.Model):
    number = models.CharField(max_length=5, unique=True)
    title = models.CharField(max_length=10)
    credits = models.IntegerField()


class Professor(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    departament = models.CharField(max_length=10)
    salary = models.IntegerField()
    rank = models.CharField(max_length=10)
    age = models.IntegerField()

    class Meta:
        unique_together = ("first_name", "last_name")


class Take(models.Model):
    student_id = models.BigIntegerField()
    course_number = models.CharField(max_length=5)

    class Meta:
        unique_together = ("student_id", "course_number")


class Teach(models.Model):
    professor_first_name = models.CharField(max_length=10)
    professor_last_name = models.CharField(max_length=10)
    course_id = models.BigIntegerField()
