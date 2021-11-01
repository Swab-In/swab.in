from .models import Forum
from lokasi.models import Post
from django.shortcuts import render

# Create your views here.
# def index(request):
#     forums = Forum.objects.all()
#     lokasi = Post.objects.all()
    
#     response = {
#         'forums': forums, 
#         'lokasi' : lokasi,
#         }

#     return render(request, 'forum/list_forum.html', response)