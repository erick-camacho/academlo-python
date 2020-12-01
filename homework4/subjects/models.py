from django.db import models

from professors.models import Professor


class Subject(models.Model):
    name = models.CharField(max_length=255)
    credits = models.IntegerField()
    professors = models.ManyToManyField(Professor, related_name='professors')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
