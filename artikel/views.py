from django.shortcuts import render
from .models import *
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from django.core import serializers
from django.http.response import HttpResponse, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model;

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
def artikel_cards(request):
    res = []
    obj = Post.objects.all()

    print('Something')
    for i in obj:
        res.append({
            "pk": i.pk,
            "judul" : i.judul,
            "foto" : i.foto,
            "author" : i.author,
            "isi" : i.isi
        })

    res = json.dumps(res)

    return HttpResponse(res, content_type='application/json')


@csrf_exempt
def add_comment(request):
    newData = json.loads(request.body.decode('utf-8'))
    print(newData)

    users = get_user_model().objects.all()
    for u in users:
        if u.username == newData["user_id"]:
            get_penulis = u

    obj = Post.objects.all()
    for i in obj:
        if i.pk == newData["post_id"]:
            get_comment = i

    new_exp = Comment(
        user_id = get_comment,
        penulis = get_penulis,
        komen = newData['komen'],
    )

    new_exp.save()
    return JsonResponse({"instance": "Komentar Disimpan"}, status=200)

@csrf_exempt
def get_comment(request):
    res = []
    obj = Comment.objects.all()

    print('uye')
    for i in obj:
        res.append({
            "post_id" : i.post_id.pk,
            "komen" : i.komen,
            "user_id" : i.user_id.username,
        })

    res = json.dumps(res)

    return HttpResponse(res, content_type='application/json')

    
# @csrf_exempt
# def comment_post(request):
#     body_unicode = request.body.decode('utf-8')

#     body = json.loads(body_unicode)

#     komen = body['komen']
#     post_id = body['post_id']
#     user_id = body['user_id']

#     post = Post.objects.filter(pk=post_id)[0]

#     User = get_user_model()

#     users = User.objects.filter(id=user_id)[0] 
    
#     comment = Comment.objects.create(post_id = post, comment=komen, user_id = users)
#     comment.save()

#     res = []
#     print(comment.komentar)
#     res.append({
#             "comment" : comment.komentar,
#             "user_id" : comment.user_id.username,
#         })

#     res = json.dumps(res)

#     return HttpResponse(res, content_type='application/json', status=200)