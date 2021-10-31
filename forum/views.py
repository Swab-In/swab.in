from .models import Forum
from .forms import ForumForm
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    forums = Forum.objects.all()
    response = {
        'forums': forums, 
        }

    form = ForumForm(request.POST or None)

    if (form.is_valid() and request.method == 'POST'):
        forum = Forum.objects.create(writer = User.objects.get(pk=request.user.id))
        forum.title = form.cleaned_data['title']
        forum.message = form.cleaned_data['message']
        forum.image = form.cleaned_data['image']
        forum.save()
        return HttpResponseRedirect('/forum')
    
    response = {
        'forums': forums, 
        'form' : form
        }

    return render(request, 'forum/list_forum.html', response)

# class LokasiList(ListView):
#     model = Post
#     template_name = 'lokasi/index.html'

# class LokasiDetail(DetailView):
#     model = Forum
#     context_object_name = 'lokasi_detail'
#     template_name = 'forum/list_forum.html'