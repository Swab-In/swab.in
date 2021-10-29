from django.shortcuts import render

# Create your views here.
posts = [
    {
        'author': 'John Mason',
        'title': 'Tempat 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2222'
    },
    {
        'author': 'Jane Doe',
        'title': 'Tempat 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2222'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'lokasi/index.html', context)