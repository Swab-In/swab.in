from django.shortcuts import render
from .models import *
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from django.core import serializers
from django.http.response import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

class HomeView(ListView):
    model = Post
    template_name = 'index.html'
    
class ArticleDetail(FormMixin, DetailView):
    model = Post
    template_name = 'base_artikel.html'
    context_object_name = "artikel_detail"
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        ctx = super(ArticleDetail, self).get_context_data(**kwargs)
        ctx['komentar'] = Comment.objects.all().filter(post_id=ctx['artikel_detail'].pk)
        ctx['form'] = CommentForm(initial={'post': self.object})
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
        ctx = super(ArticleDetail, self).get_context_data(**kwargs)
        print(ctx)
        komen = Comment.objects.create(post_id = ctx['artikel_detail'],
        komen = form.cleaned_data["komen"], user_id = request.user)
        print(komen)
        komen.save()
        return super(ArticleDetail, self).form_valid(form)

# json
def json_req(request):
    data = serializers.serialize('json', Comment.objects.all())
    print(data)
    return HttpResponse(data, content_type="application/json")

@csrf_exempt
def artikel_content(request):
    res = []
    obj = Post.objects.all()

    print('Something')
    for i in obj:
        res.append({
            "judul" : i.judul,
            "author" : i.author,
            "foto" : i.foto,
        })

    res = json.dumps(res)

    return HttpResponse(res, content_type='application/json')