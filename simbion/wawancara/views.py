from django.shortcuts import render
from .forms import WawancaraForm

response = {}


def index(request):
    response['author'] = 'Benny William Pardede'
    response['form_wawancara'] = WawancaraForm
    html = 'wawancara/wawancara.html'
    return render(request, html, response)
