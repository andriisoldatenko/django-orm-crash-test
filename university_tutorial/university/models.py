from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField()


class Course(models.Model):
    title = models.CharField(max_length=10)
    credits = models.IntegerField()


class Professor(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    departament = models.CharField(max_length=10)
    salary = models.IntegerField()
    rank = models.CharField(max_length=10)
    age = models.IntegerField()


class Take(models.Model):
    student_id = models.BigIntegerField()
    course_id = models.BigIntegerField()


class Teach(models.Model):
    professor_first_name = models.CharField(max_length=10)
    professor_last_name = models.CharField(max_length=10)
    course_id = models.BigIntegerField()
