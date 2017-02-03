#!/usr/bin/env python
import os
import sys
import django

# We need configure the enviroment before using any django module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo.settings')
sys.path += ['../demo']
django.setup()

from university.models import (
    Student,
    Course,
    Professor,
    Take,
    Teach
)


def main():
    students = (
        ('AARON', 20), ('CHUCK', 21), ('DOUG', 20), ('MAGGIE', 19),
        ('STEVE', 22), ('JING', 18), ('BRIAN', 21), ('KAY', 20),
        ('GILLIAN', 20), ('CHAD', 21)
    )

    courses = (
        ('CS112', 'PHYSICS', 4),
        ('CS113', 'CALCULUS', 4),
        ('CS114', 'HISTORY', 4)
    )

    professors = (
        ('ALEX', 'CHOI', 'SCIENCE', 400, 1, 45),
        ('DAVID', 'GUNN', 'HISTORY', 300, 2, 60),
        ('STEVE', 'MAYER', 'MATH', 400, 2, 55),
        ('GARRY', 'POMEL', 'SCIENCE', 500, 1, 65),
        ('TITI', 'FEUER', 'MATH', 400, 3, 40)
    )

    takes = (
        (1, 'CS112'),
        (1, 'CS113'),
        (1, 'CS114'),
        (2, 'CS112'),
        (3, 'CS112'),
        (3, 'CS114'),
        (4, 'CS112'),
        (4, 'CS113'),
        (5, 'CS113'),
        (6, 'CS113'),
        (6, 'CS114')
    )
    takes = (
        ('AARON', 'CS112'),
        ('AARON', 'CS113'),
        ('AARON', 'CS114'),
        ('CHUCK', 'CS112'),
        ('DOUG', 'CS112'),
        ('DOUG', 'CS114'),
        ('MAGGIE', 'CS112'),
        ('MAGGIE', 'CS113'),
        ('STEVE', 'CS113'),
        ('JING', 'CS113'),
        ('JING', 'CS114')
    )

    teach_ = (
        ('CHOI', 'CS112'),
        ('CHOI', 'CS113'),
        ('CHOI', 'CS114'),
        ('POMEL', 'CS113'),
        ('MAYER', 'CS112'),
        ('MAYER', 'CS114')
    )
    if not Student.objects.all():
        for student in students:
            Student.objects.create(name=student[0], age=student[1])

    if not Course.objects.all():
        for course in courses:
            Course.objects.create(number=course[0], title=course[1],
                                  credits=course[2])

    if not Professor.objects.all():
        for professor in professors:
            Professor.objects.create(
                first_name=professor[0], last_name=professor[1],
                departament=professor[2], salary=professor[3],
                rank=professor[3], age=professor[4]
            )

    if not Take.objects.all():
        for take in takes:
            Take.objects.create(
                student=Student.objects.get(name=take[0]),
                course=Course.objects.get(number=take[1])
            )

    if not Teach.objects.all():
        for teach in teach_:
            Teach.objects.create(
                professor=Professor.objects.get(last_name=teach[0]),
                course=Course.objects.get(number=teach[1])
            )

if __name__ == '__main__':
    main()
