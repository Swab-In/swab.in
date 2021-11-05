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
    
def json(request):
    id = request.GET.get('id')
    data = serializers.serialize('json', Komentar.objects.filter(forum_id=Forum.objects.filter(pk=int(id))[0]))
    return HttpResponse(data, content_type="application/json")



