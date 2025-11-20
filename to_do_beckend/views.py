from rest_framework import generics
from .models import ToDo
from .serialziers import StudentSerializer

class StudentView(generics.CreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = StudentSerializer

class StudentList(generics.ListAPIView):
    queryset = ToDo.objects.all()
    serializer_class = StudentSerializer

class StudentDetail(generics.UpdateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = StudentSerializer