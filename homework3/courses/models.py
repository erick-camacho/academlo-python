from django.db import models
from students.models import Student


class Course(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.name
