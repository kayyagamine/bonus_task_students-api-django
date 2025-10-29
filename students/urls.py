from django.urls import path
from .views import student_list, get_adult_students

urlpatterns = [
    path('students/', student_list, name='students'),
    path('students/adults/', get_adult_students, name='adult-students'),
]
