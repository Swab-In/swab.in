from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'lokasi/index.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class PostDetailView(DetailView):
    model = Post 

class PostCreateView(CreateView, LoginRequiredMixin):
    model = Post
    fields = ['title', 'content']

    # Set current author
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)