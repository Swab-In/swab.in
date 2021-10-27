from django.shortcuts import render
from .models import Komentar
from .forms import NoteForm
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    note = Komentar.objects.all().values()  # TODO Implement this
    response = {'note': note}
    return render(request, 'index.html', response)

def add_comment(request):
    context ={}

    # create object of form
    form = NoteForm(request.POST or None, request.FILES or None)
    
    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()
        if request.method == "POST" :
            return HttpResponseRedirect('/artikel')

    context['form']= form
    return render(request, "index.html", context)