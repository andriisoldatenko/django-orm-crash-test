from django.db import models


class Student(models.Model):
    number = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)
    age = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'student'


class Course(models.Model):
    number = models.CharField(max_length=5, primary_key=True)
    title = models.CharField(max_length=10)
    credits = models.IntegerField()

    class Meta:
        db_table = 'course'


class Professor(models.Model):
    # By default, Django gives each model the following field
    # if there is no primary_key=True in
    # id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    departament = models.CharField(max_length=10)
    salary = models.IntegerField()
    rank = models.CharField(max_length=10)
    age = models.IntegerField()

    class Meta:
        db_table = 'professor'
        unique_together = ("first_name", "last_name")


class Take(models.Model):
    student = models.ForeignKey(Student)
    course = models.ForeignKey(Course)

    class Meta:
        db_table = 'take'
        unique_together = ("student", "course")


class Teach(models.Model):
    professor = models.ForeignKey(Professor)
    course = models.ForeignKey(Course)

    class Meta:
        db_table = 'teach'
        unique_together = ("professor", "course")
