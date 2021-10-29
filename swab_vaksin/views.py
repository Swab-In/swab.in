from django.http.response import HttpResponseRedirect

from swab_vaksin.models import SwabInformation, VaksinInformation, Experience
from swab_vaksin.forms import PengalamanForm
from django.shortcuts import render
from .models import Experience
from django.contrib.auth.models import User

def index(request):
    return render(request, 'list_vaksin_swab.html')

def informasi(request):
    experiences = Experience.objects.all()
    response = {
        'experiences': experiences, 
        }

    form =  PengalamanForm(request.POST or None)

    if (form.is_valid() and request.method == 'POST'):
        pengalaman = Experience.objects.create(penulis = User.objects.get(pk=request.user.id), 
        pengalaman= form.cleaned_data["pengalaman"])
        pengalaman.save()
        return HttpResponseRedirect('/swab-vaksin/informasi')
    
    response['form']= form

    return render(request, 'informasi_vaksin_swab.html', response)

# def informasi(request):
# #     context = {}
#     form =  PengalamanForm(request.POST or None)
#     if (form.is_valid and request.method == 'POST'):
#         form.save()
#         return HttpResponseRedirect('/swab-vaksin/informasi')
    
#     context['form']= form
#     return render(request, 'informasi_vaksin_swab.html', context)