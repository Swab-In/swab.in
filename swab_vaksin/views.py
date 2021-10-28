from django.http.response import HttpResponseRedirect

from swab_vaksin.models import Informasi
from django.shortcuts import render

def index(request):
    return render(request, 'list_vaksin_swab.html')

def add_pengalaman(request):
    return render(request, 'add_pengalaman.html')

def informasi(request):
    return render(request, 'informasi_vaksin_swab.html')