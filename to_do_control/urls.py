from django.contrib import admin
from django.urls import path, include
from to_do_beckend.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('maenu/', include('to_do_beckend.urls')),
]
