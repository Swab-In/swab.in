from django.http.response import HttpResponseRedirect

from swab_vaksin.models import SwabInformation, VaksinInformation, Experience
from swab_vaksin.forms import PengalamanForm
from django.shortcuts import render

def index(request):
    return render(request, 'list_vaksin_swab.html')

def informasi(request):
    experiences = Experience.objects.all()
    response = {
        'experiences': experiences, 
        'form': '',
        }

    form =  PengalamanForm(request.POST or None)
    if (form.is_valid and request.method == 'POST'):
        form.save()
        return HttpResponseRedirect('/swab-vaksin/informasi')
    
    response['form']= form

    return render(request, 'informasi_vaksin_swab.html', response)

# def informasi(request):
#     context = {}
    form =  PengalamanForm(request.POST or None)
    if (form.is_valid and request.method == 'POST'):
        form.save()
        return HttpResponseRedirect('/swab-vaksin/informasi')
    
    context['form']= form
#     return render(request, 'informasi_vaksin_swab.html', context)