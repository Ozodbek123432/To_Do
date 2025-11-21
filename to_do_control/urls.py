from django.contrib import admin
from django.urls import path, include
from to_do_beckend.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('home/',include('to_do_beckend.urls')),
]
