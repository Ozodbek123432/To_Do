from django.contrib import admin
from django.urls import path, include
from .views import TodoView,ToDoList,ToDoDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', TodoView.as_view(),name="malumoaltni korish"),
    path('create/', ToDoList.as_view(),name='malumoaltarni yaraytish'),
    path('detail/<int:pk>/`x', ToDoDetail.as_view(),name = "malumoatlarni ochirish"),
]