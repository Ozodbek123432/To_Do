from rest_framework import generics
from .models import ToDo
from .serialziers import ToDoSerializer

class TodoView(generics.CreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class ToDoList(generics.ListAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class ToDoDetail(generics.UpdateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer