from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student, University
from .serializers import StudentSerializer, UniversitySerializer


@api_view(['POST'])
def add_university(request):
    serializer = UniversitySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "University added successfully", "data": serializer.data})
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def get_all_universities(request):
    universities = University.objects.all()
    serializer = UniversitySerializer(universities, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_student(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Student added successfully", "data": serializer.data})
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def get_all_students(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_students_by_university(request, university_id):
    try:
        university = University.objects.get(id=university_id)
        students = university.students.all()  # استخدام related_name
        serializer = StudentSerializer(students, many=True)
        return Response({
            "university": university.name,
            "students": serializer.data
        })
    except University.DoesNotExist:
        return Response({"error": "University not found"}, status=404)