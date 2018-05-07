from django.urls import path

from .views import *

app_name = 'pengumuman'

urlpatterns = [
    path('', index, name='index'),
    path('<int:index>', content, name='content')
]
