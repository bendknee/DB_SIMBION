from django.urls import path
from .views import index

app_name = 'lihat_beasiswa'

urlpatterns = [
	path('', index, name='index'),
]