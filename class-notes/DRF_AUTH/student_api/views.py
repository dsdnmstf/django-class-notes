from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from django.shortcuts import HttpResponse
from .models import Student
from .serializers import StudentSerializer
from rest_framework import generics

# Create your views here.
def home(request):
    return HttpResponse('<h1>API Page</h1>')

class StudentList(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    # permission_classes = [IsAdminUser]
    permission_classes = [ IsAuthenticatedOrReadOnly]
    
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

class StudentOperations(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()