from django.contrib.auth.models import User
from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView

def index(request):
    swabInformations = SwabInformation.objects.all()
    vaksinInformations = VaksinInformation.objects.all()

    response = {
        'swabInformations': swabInformations, 
        'vaksinInformations': vaksinInformations,
        }
    
    return render(request, "list_vaksin_swab.html", response)

def informasiSwab(request):
    swabExperiences = SwabExperience.objects.all()
    response = {
        'swabExperiences': swabExperiences, 
        }

    form =  PengalamanSwabForm(request.POST or None)

    if (form.is_valid() and request.method == 'POST'):
        pengalaman = SwabExperience.objects.create(penulis = User.objects.get(pk=request.user.id), 
        pengalaman = form.cleaned_data["pengalaman"])
        pengalaman.save()
        return HttpResponseRedirect('/swab-vaksin/informasi')
    
    response['form']= form

    return render(request, "info_swab.html", response)

def informasiVaksin(request):
    vaksinExperiences = VaksinExperience.objects.all()
    response = {
        'vaksinExperiences': vaksinExperiences, 
        }

    form =  PengalamanVaksinForm(request.POST or None)

    if (form.is_valid() and request.method == 'POST'):
        pengalaman = VaksinExperience.objects.create(penulis = User.objects.get(pk=request.user.id), 
        pengalaman = form.cleaned_data["pengalaman"])
        pengalaman.save()
        return HttpResponseRedirect('/swab-vaksin/informasi')
    
    response['form']= form

    return render(request, "info_vaksin.html", response)

class InfoList(ListView):
    model = SwabInformation, VaksinInformation
    template_name = "templates/list_vaksin_swab.html"

class InfoDetailSwab(DetailView):
    model = SwabInformation
    context_object_name = 'informasi_swab'
    form = PengalamanSwabForm
    template_name = "info_swab.html"
    
    def get_context_data(self, **kwargs):
        ctx = super(InfoDetailSwab, self).get_context_data(**kwargs)
        ctx['sExperience'] = SwabExperience.objects.all().filter(swab_id=ctx['informasi_swab'].pk)
        ctx['form'] = PengalamanSwabForm
        print(ctx['sExperience'])
        return ctx

class InfoDetailVaksin(DetailView):
    model = VaksinInformation
    context_object_name = 'informasi_vaksin'
    form = PengalamanVaksinForm
    template_name = "info_vaksin.html"
    
    def get_context_data(self, **kwargs):
        ctx = super(InfoDetailVaksin, self).get_context_data(**kwargs)
        ctx['vExperience'] = VaksinExperience.objects.all().filter(vaksin_id=ctx['informasi_vaksin'].pk)
        ctx['form'] = PengalamanVaksinForm
        print(ctx['vExperience'])
        return ctx
