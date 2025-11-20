from rest_framework import generics
from .models import ToDo
from .serialziers import ToDoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
class TodoView(generics.CreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class ToDoList(generics.ListAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer


class ToDoDetail(APIView):
    def patch(self, request, pk):
        try:
            todo = ToDo.objects.get(pk=pk)
        except ToDo.DoesNotExist:
            return Response({"error": "Topilmadi"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ToDoSerializer(todo, data=request.data, partial=True)  # partial=True — muhim!
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)