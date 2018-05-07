from django.urls import path

from .views import daftar_beasiswa, tambah_beasiswa_aktif

app_name = 'daftar_beasiswa'

urlpatterns = [
    path('baru/', daftar_beasiswa, name='daftar-beasiswa'),
    path('tambah/', tambah_beasiswa_aktif, name='tambah-beasiswa-aktif')
]