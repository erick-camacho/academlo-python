from django.shortcuts import get_object_or_404, render
from .models import Student


def all_students(request):
    students = Student.objects.all()
    return render(request, 'students/index.html', {'students': students})


def student_details(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return render(request, 'students/detail.html', {'student': student})
