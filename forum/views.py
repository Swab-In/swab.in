from django.contrib.auth import get_user_model
from django.shortcuts import render

from .models import Forum, Komentar
from .forms import ForumForm
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.core import serializers
from django.http.response import HttpResponse, JsonResponse
from .forms import *
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json 

def index(request):
    return render(request, 'forum/list_forum.html')


class List_forumView(ListView):
    model = Forum
    template_name = "forum/list.html"

class ForumDetail(DetailView, FormMixin, LoginRequiredMixin):
    model = Forum
    context_object_name = 'forum_detail'
    template_name = "forum/forum_detail.html"
    form_class = KomentarForm
    
    # Query komentar and update to context
    def get_context_data(self, **kwargs):
        ctx = super(ForumDetail, self).get_context_data(**kwargs)
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
    
    def form_valid(self, form, request, **kwargs):
        
        ctx = super(ForumDetail, self).get_context_data(**kwargs)
        forum = Komentar.objects.create(forum_id = ctx['forum_detail'],
         komentar = form.cleaned_data["komentar"],
         user_id = request.user)
        forum.save()
        return super(ForumDetail, self).form_valid(form)

@csrf_exempt
def json_req(request):
    # id = request.GET.get('id')
    # print(id)
    data = serializers.serialize('json', Komentar.objects.all())
    return HttpResponse(data, content_type="application/json")

@csrf_exempt
def json_forum(request):
    data = serializers.serialize('json', Forum.objects.all())
    return HttpResponse(data, content_type="application/json")

@csrf_exempt
def json_lokasi(request):
    data = serializers.serialize('json', Post.objects.all())
    return HttpResponse(data, content_type="application/json")

@csrf_exempt
def add_forum(request):
    newData = json.loads(request.body.decode('utf-8'))

    users = get_user_model().objects.all()
    for j in users:
        if j.pk == newData["writer"]:
            get_writer = j

    obj = Post.objects.all()
    for i in obj:
        if i.pk == newData["post_id"]:
            get_post = i

    new_forum = Forum(
        title = newData['title'],
        message = newData['message'],
        image = newData['image'],
        writer = get_writer,
        post_id = get_post)

    new_forum.save()
    return JsonResponse({"instance": "Forum Disimpan"}, status=200)
