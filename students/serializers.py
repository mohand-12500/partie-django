from rest_framework import serializers
from .models import Student, University

class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ['id', 'name']

class StudentSerializer(serializers.ModelSerializer):

    university_details = UniversitySerializer(source='university', read_only=True)
    
    class Meta:
        model = Student
        fields = ['id', 'name', 'address', 'university', 'university_details']
        
    
    def to_representation(self, instance):
        data = super().to_representation(instance)

        if not instance.university:
            data.pop('university_details', None)
        return data