from django.urls import path
from .views import index, detail_beasiswa

app_name = 'lihat_beasiswa'

urlpatterns = [
	path('', index, name='index'),
	path('detail/', detail_beasiswa, name='detail-beasiswa'),
]