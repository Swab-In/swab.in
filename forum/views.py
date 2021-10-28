from django.shortcuts import render
from .models import Forum
from .forms import ForumForm

# Create your views here.
def index(request):
    return render(request, 'forum/index.html')

def list(request):
    forum = Forum.objects.all().values()
    response = {'forums': forum}
    return render(request, 'forum/list-forum.html')