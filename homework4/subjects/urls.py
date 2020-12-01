from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('subjects/', views.subject_list),
    path('subjects/<int:pk>/', views.subject_detail)
]

urlpatterns = format_suffix_patterns(urlpatterns)
