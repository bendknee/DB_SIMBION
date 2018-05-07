from django.urls import path

from .views import index

app_name = 'wawancara'

urlpatterns = [
    path('', index, name='index'),
]
