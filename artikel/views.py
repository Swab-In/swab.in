from django.shortcuts import render
from .models import *
from .forms import NoteForm
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView

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

class HomeView(ListView):
    model = Post
    template_name = 'index.html'
    
class ArticleDetail(DetailView):
    model = Post
    template_name = 'base_artikel.html'
    context_object_name = "artikel_detail"

    def get_context_data(self, **kwargs):
        ctx = super(ArticleDetail, self).get_context_data(**kwargs)
        ctx['komentar'] = Komentar.objects.all().filter(post_id=ctx['artikel_detail'].pk)
        return ctx