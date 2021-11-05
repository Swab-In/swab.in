from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.core import serializers
from django.shortcuts import render
from django.views.generic.edit import FormMixin
from .models import *
from .forms import *
from django.views.generic import *

def index(request):
    swabInformations = SwabInformation.objects.all()
    vaksinInformations = VaksinInformation.objects.all()

    response = {
        'swabInformations': swabInformations, 
        'vaksinInformations': vaksinInformations,
        }
    
    return render(request, "list_vaksin_swab.html", response)

class InfoDetailSwab(DetailView, FormMixin):
    model = SwabInformation
    context_object_name = 'informasi_swab'
    form_class = PengalamanSwabForm
    template_name = "info_swab.html"
    
    def get_context_data(self, **kwargs):
        ctx = super(InfoDetailSwab, self).get_context_data(**kwargs)
        ctx['sExperience'] = SwabExperience.objects.all().filter(swab_id=ctx['informasi_swab'].pk)
        return ctx

    def get_success_url(self):
        return self.request.path

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form, request)
        else:
            return self.form_invalid(form)
    
    def json(request):
        data = serializers.serialize('json', SwabExperience.objects.all())
        return HttpResponse(data, content_type="application/json")

    def form_valid(self, form, request, **kwargs):
        ctx = super(InfoDetailSwab, self).get_context_data(**kwargs)
        swab = SwabExperience.objects.create(
            swab_id = ctx['informasi_swab'],
            penulis = request.user,
            pengalamanSwab = form.cleaned_data["pengalamanSwab"]
            )
        swab.save()
        return super(InfoDetailSwab, self).form_valid(form)

class InfoDetailVaksin(DetailView, FormMixin):
    model = VaksinInformation
    context_object_name = 'informasi_vaksin'
    form_class = PengalamanVaksinForm
    template_name = "info_vaksin.html"
    
    def get_context_data(self, **kwargs):
        ctx = super(InfoDetailVaksin, self).get_context_data(**kwargs)
        ctx['vExperience'] = VaksinExperience.objects.all().filter(vaksin_id=ctx['informasi_vaksin'].pk)
        return ctx


    def get_success_url(self):
        return self.request.path

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form, request)
        else:
            return self.form_invalid(form)
    
    def json(request):
        data = serializers.serialize('json', VaksinExperience.objects.all())
        return HttpResponse(data, content_type="application/json")

    def form_valid(self, form, request, **kwargs):
        ctx = super(InfoDetailVaksin, self).get_context_data(**kwargs)
        vaksin = VaksinExperience.objects.create(
            vaksin_id = ctx['informasi_vaksin'],
            penulis = request.user,
            pengalamanVaksin = form.cleaned_data["pengalamanVaksin"]
            )
        vaksin.save()
        return super(InfoDetailVaksin, self).form_valid(form)

# def informasiSwab(request):
#     swabExperiences = SwabExperience.objects.all()
#     response = {
#         'swabExperiences': swabExperiences, 
#         }

#     form =  PengalamanSwabForm(request.POST or None)

#     if (form.is_valid() and request.method == 'POST'):
#         pengalaman = SwabExperience.objects.create(penulis = User.objects.get(pk=request.user.id), 
#         pengalaman = form.cleaned_data["pengalaman"])
#         pengalaman.save()
#         return HttpResponseRedirect('/swab-vaksin/informasi')
    
#     response['form']= form

#     return render(request, "info_swab.html", response)

# def informasiVaksin(request):
#     vaksinExperiences = VaksinExperience.objects.all()
#     response = {
#         'vaksinExperiences': vaksinExperiences, 
#         }

#     form =  PengalamanVaksinForm(request.POST or None)

#     if (form.is_valid() and request.method == 'POST'):
#         pengalaman = VaksinExperience.objects.create(penulis = User.objects.get(pk=request.user.id), 
#         pengalaman = form.cleaned_data["pengalaman"])
#         pengalaman.save()
#         return HttpResponseRedirect('/swab-vaksin/informasi')
    
#     response['form']= form

#     return render(request, "info_vaksin.html", response)

# class InfoList(ListView):
#     model = SwabInformation, VaksinInformation
#     template_name = "templates/list_vaksin_swab.html"

