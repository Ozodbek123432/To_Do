from rest_framework import generics
from .models import ToDo
from .serialziers import ToDoSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login

class TodoView(generics.CreateAPIView):
    authentication_classes = [SessionAuthentication]  # Kimligingizni qanday tekshiraman?
    permission_classes = [IsAuthenticated]
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class ToDoList(generics.ListAPIView):
    authentication_classes = [SessionAuthentication]  # Kimligingizni qanday tekshiraman?
    permission_classes = [IsAuthenticated]
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class ToDoDetail(APIView):
    def patch(self, request, pk):
        try:
            todo = ToDo.objects.get(pk=pk)
        except ToDo.DoesNotExist:
            return Response({"error": "Topilmadi"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ToDoSerializer(todo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MyHomePageView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": f"Welcome {request.user.email}!"})


class LoginView(APIView):
    def post(self, request):
        # Match credentials to a user in the database
        user = authenticate(
            request,
            username=request.data.get('username'),
            password=request.data.get('password')
        )

        if user:
            # Create a user session and attach authentication cookie to
            login(request, user)
            return Response({"status": "Logged in"})
        return Response({"error": "Invalid credentials"}, status=400)