from django.contrib import admin
from django.urls import path, include
from .views import TodoView,ToDoList,ToDoDetail,MyHomePageView


urlpatterns = [
    path('list/', ToDoList.as_view(),name="malumoaltni korish"),
    path('create/', TodoView.as_view(),name='malumoaltarni yaraytish'),
    path('patch/<int:pk>/', ToDoDetail.as_view(),name = "yanqilash"),

]