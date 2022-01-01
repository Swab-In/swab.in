from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Pesan
from .forms import ContactForm
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def index(request):
    return render(request, 'about.html')

def contactus(request):
    context = {}

    form = ContactForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        if request.method == 'POST' :
            return HttpResponseRedirect("/about/contact")
    
    context['form'] = form
    return render(request, 'contact.html', context)

def func_json(request):
    data = serializers.serialize('json', Pesan.objects.all())
    return HttpResponse(data, content_type="application/json")

def listcontact(request):
    return render(request, 'list_message.html')

@csrf_exempt
def pesan_post(request):
    body_unicode = request.body.decode('utf-8')

    body = json.loads(body_unicode)

    first = body['first']
    last = body['last']
    email = body['email']
    no_hp = body['no_hp']
    message = body['message']

    print(first)
    pesan = Pesan.objects.create(first=first, last=last, email=email, no_hp=no_hp, message=message)
    pesan.save()

    return HttpResponse(pesan, content_type="application/json", status=201)

@csrf_exempt
def semua_pesan(request):
    pesan = Pesan.objects.all

    res = []
    for i in pesan:
        res.append({
            "first" : i.first,
            "last" : i.last,
            "email" : i.email,
            "no_hp" : i.no_hp,
            "message" : i.message,
        })
    res = json.dumps(res)

    return HttpResponse(res, content_type="application/json")



