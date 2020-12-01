from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('professors/', views.professor_list),
    path('professors/<int:pk>/', views.professor_detail)
]

urlpatterns = format_suffix_patterns(urlpatterns)
