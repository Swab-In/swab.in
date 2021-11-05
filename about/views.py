from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Pesan
from .forms import ContactForm
from django.core import serializers

# Create your views here.
def index(request):
    return render(request, 'about.html')

# @login_required(login_url='/admin/login/')
def contactus(request):
    context = {}

    form = ContactForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        if request.method == 'POST' :
            return HttpResponseRedirect("/about/contact")
    
    context['form'] = form
    return render(request, 'contact.html', context)

def json(request):
    data = serializers.serialize('json', Pesan.objects.all())
    return HttpResponse(data, content_type="application/json")

def listcontact(request):
    return render(request, 'list_message.html')