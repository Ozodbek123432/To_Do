from django.contrib import admin
from django.urls import path, include
from .views import StudentView,StudentList,StudentDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', StudentList.as_view(),name='list'),
    path('create/', StudentView.as_view(),name='create'),
    path('detail/<int:pk>/`x', StudentDetail.as_view(),name='detail'),
]