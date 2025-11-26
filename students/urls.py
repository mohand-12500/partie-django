from django.urls import path
from . import views

urlpatterns = [
    
    path('university/add/', views.add_university, name='add_university'),
    path('university/getAll/', views.get_all_universities, name='get_all_universities'),
    
    
    path('student/add/', views.add_student, name='add_student'),
    path('student/getAll/', views.get_all_students, name='get_all_students'),
    path('student/byUniversity/<int:university_id>/', views.get_students_by_university, name='get_students_by_university'),
]