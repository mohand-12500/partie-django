from django.contrib import admin
from .models import University, Student

@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'address', 'university']
    list_filter = ['university']