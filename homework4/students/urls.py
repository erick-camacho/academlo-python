from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns 
from . import views

urlpatterns = [
    path('students/', views.student_list),
    path('students/<int:pk>/', views.student_detail)
]

urlpatterns = format_suffix_patterns(urlpatterns)
