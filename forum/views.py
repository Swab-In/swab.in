from django.shortcuts import render
from .models import Forum, Komentar
from .forms import ForumForm
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.core import serializers
from django.http.response import HttpResponse
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
def forum_content(request):
    res = []
    obj = Forum.objects.all()
    for i in obj:
        res.append( {
            "title" : i.title,
            "image" : i.image
        })
    res = json.dumps(res)


    return HttpResponse(res, content_type='application/json')

@csrf_exempt
def komentar_post(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    content = body['title']
    print(content)
    return HttpResponse(status=201)



