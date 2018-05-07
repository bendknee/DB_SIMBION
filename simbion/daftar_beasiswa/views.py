from django.shortcuts import render
from .forms import Daftar_Beasiswa_Form, Tambah_Beasiswa_Aktif_Form

response = {"author" : "Ahmad Hasan Siregar"}

def daftar_beasiswa(request):
	html = "daftar_beasiswa/daftar_beasiswa.html"
	response["daftar_beasiswa_form"] = Daftar_Beasiswa_Form
	return render(request, html, response)

def tambah_beasiswa_aktif(request):
	html = 'daftar_beasiswa/tambah_beasiswa_aktif.html'
	response["tambah_beasiswa_aktif_form"] = Tambah_Beasiswa_Aktif_Form
	return render(request, html, response)