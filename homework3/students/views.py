from django.shortcuts import get_object_or_404, render
from .models import Student
from courses.models import Course


def index(request):
    students = Student.objects.all()
    return render(request, 'students/index.html', {'students': students})


def detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    courses = Course.objects.filter(students__pk=student_id)
    return render(request, 'students/detail.html', {
        'student': student,
        'courses': courses
    })
