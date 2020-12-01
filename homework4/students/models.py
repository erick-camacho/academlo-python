from django.db import models

from subjects.models import Subject


class Student(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    telephone = models.CharField(max_length=10)
    email = models.EmailField()
    subjects = models.ManyToManyField(Subject, related_name='subjects')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
