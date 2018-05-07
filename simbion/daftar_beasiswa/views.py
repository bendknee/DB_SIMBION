from django.shortcuts import render

# Create your views here.
response = {"author" : "Ahmad Hasan Siregar"}

def index(request):
	html = "daftar_beasiswa/daftar_beasiswa.html"
	return render(request, html, response)