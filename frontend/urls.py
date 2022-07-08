from django.urls import path
from .views import *

urlpatterns = [
    path('', welcome, name='frontend-welcome'),
    path('main/', main, name='frontend-main'),
]
