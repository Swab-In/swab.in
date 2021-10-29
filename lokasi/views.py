from django.shortcuts import render
from .models import Post


def index(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'lokasi/index.html', context)