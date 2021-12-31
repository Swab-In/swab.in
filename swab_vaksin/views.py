from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.http.response import HttpResponse, JsonResponse
from django.core import serializers
from django.shortcuts import render
from django.views.generic.edit import FormMixin
from .models import *
from .forms import *
from django.views.generic import *
from django.views.decorators.csrf import csrf_exempt
import json 

@csrf_exempt
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

    def form_valid(self, form, request, **kwargs):
        ctx = super(InfoDetailVaksin, self).get_context_data(**kwargs)
        vaksin = VaksinExperience.objects.create(
            vaksin_id = ctx['informasi_vaksin'],
            penulis = request.user,
            pengalamanVaksin = form.cleaned_data["pengalamanVaksin"]
            )
        vaksin.save()
        return super(InfoDetailVaksin, self).form_valid(form)

@csrf_exempt
def jsonVaksin(request):
    data = serializers.serialize('json', VaksinExperience.objects.all())
    return HttpResponse(data, content_type="application/json")

@csrf_exempt
def jsonSwab(request):
    data = serializers.serialize('json', SwabExperience.objects.all())
    return HttpResponse(data, content_type="application/json")

@csrf_exempt
def jsonInfoSwab(request):
    data = serializers.serialize('json', SwabInformation.objects.all())
    return HttpResponse(data, content_type="application/json")

@csrf_exempt
def jsonInfoVaksin(request):
    data = serializers.serialize('json', VaksinInformation.objects.all())
    return HttpResponse(data, content_type="application/json")

@csrf_exempt
def addExperienceSwab(request):
    newData = json.loads(request.body.decode('utf-8'))
    print(newData)

    users = get_user_model().objects.all()
    for u in users:
        if u.username == newData["penulis"]:
            get_writer = u

    obj = SwabInformation.objects.all()
    for i in obj:
        if i.pk == newData["swab_id"]:
            get_exp = i

    new_exp = SwabExperience(
        swab_id = get_exp,
        penulis = get_writer,
        pengalamanSwab = newData['pengalamanSwab'],
    )

    new_exp.save()
    return JsonResponse({"instance": "Forum Disimpan"}, status=200)

@csrf_exempt
def addExperienceVaksin(request):
    newData = json.loads(request.body.decode('utf-8'))
    print(newData)

    users = get_user_model().objects.all()
    for u in users:
        if u.username == newData["penulis"]:
            get_writer = u

    obj = VaksinInformation.objects.all()
    for i in obj:
        if i.pk == newData["vaksin_id"]:
            get_exp = i

    new_exp = VaksinExperience(
        vaksin_id = get_exp,
        penulis = get_writer,
        pengalamanVaksin = newData['pengalamanVaksin'],
    )

    new_exp.save()
    return JsonResponse({"instance": "Forum Disimpan"}, status=200)