from django.urls import path

from .views import index

app_name = 'daftar_beasiswa'

urlpatterns = [
    path('', index, name='index'),
]