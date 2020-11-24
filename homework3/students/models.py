from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100, default="")
    phone = models.CharField(max_length=10, default="")
    address = models.CharField(max_length=300, default="")
    grade = models.IntegerField(default=0)

    def __str__(self):
        return self.name
