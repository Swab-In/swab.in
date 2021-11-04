from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.views.generic.edit import FormMixin
from .models import Post
from forum.models import Forum
from forum.forms import ForumForm
from django.http.response import HttpResponse
from django.core import serializers
from django.contrib.auth.models import User

class PostListView(ListView):
    model = Post
    template_name = 'lokasi/index.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class PostDetailView(DetailView, FormMixin, LoginRequiredMixin):
    model = Post 
    context_object_name = 'post_detail'
    template_name = 'forum/list_forum.html'
    form_class = ForumForm

    def get_context_data(self, **kwargs):
        ctx = super(PostDetailView, self).get_context_data(**kwargs)
        ctx['forum'] = Forum.objects.all().filter(post_id=ctx['post_detail'].pk)
        return ctx
    
    def get_success_url(self):
        return self.request.path

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form, request)
        else:
            return self.form_invalid(form)
    
    def json(request):
        data = serializers.serialize('json', Forum.objects.all())
        return HttpResponse(data, content_type="application/json")

    def form_valid(self, form, request, **kwargs):
        ctx = super(PostDetailView, self).get_context_data(**kwargs)
        print(ctx)
        forum = Forum.objects.create(post_id = ctx['post_detail'],
        title = form.cleaned_data["title"],  message = form.cleaned_data["message"],
        image = form.cleaned_data["image"], writer = request.user)
        print(forum)
        forum.save()
        return super(PostDetailView, self).form_valid(form)

class PostCreateView(CreateView, LoginRequiredMixin):
    model = Post
    fields = ['title', 'content']

    # Set current author
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)