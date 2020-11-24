from django.shortcuts import get_object_or_404, render
from .models import Course


def all_courses(request):
    courses = Course.objects.all()
    return render(request, 'courses/index.html', {'courses': courses})


def course_details(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'courses/detail.html', {'course': course})
