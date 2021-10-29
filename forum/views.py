from django.shortcuts import render
from .models import Forum
from .forms import ForumForm
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request, 'forum/index.html')

# masih error
def list(request):
    forum = Forum.objects.all()
    form = ForumForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        if request.method == "POST" :
            return HttpResponseRedirect('/')
    context = {'form': form, 'forum': forum}
    return render(request, "forum/list_forum.html", context)
