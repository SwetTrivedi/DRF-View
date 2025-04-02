from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import  ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,ListCreateAPIView,RetrieveUpdateAPIView
# Create your views here.
class StudentList(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class StudentCreate(CreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer


class StudentRetrieve(RetrieveAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer


class StudentUpdate(UpdateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer


class Studentdelete(DestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer


class Studentlistcreate(ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer



class StudentRetrieveupdate(RetrieveUpdateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer