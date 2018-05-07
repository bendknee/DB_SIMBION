from django.shortcuts import render
from .forms import PembayaranForm

response = {}


def index(request):
    response['author'] = 'Benny William Pardede'
    response['form_wawancara'] = PembayaranForm
    html = 'pembayaran/pembayaran.html'
    return render(request, html, response)
