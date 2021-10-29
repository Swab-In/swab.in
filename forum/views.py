from django.shortcuts import render
from .models import Forum, Komentar
from .forms import ForumForm
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView


def index(request):
    return render(request, 'forum/list_forum.html')

# masih error
def list(request):
    forum = Forum.objects.all()
    form = ForumForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        if request.method == "POST" :
            return HttpResponseRedirect('/')
    context = {'form': form, 'forum': forum}
    return render(request, "forum/list_forum.html", context)

class List_forumView(ListView):
    model = Forum
    template_name = "forum/list.html"

class ForumDetail(DetailView):
    model = Forum
    context_object_name = 'forum_detail'
    template_name = "forum/forum_detail.html"
    
    # Query komentar and update to context
    def get_context_data(self, **kwargs):
        ctx = super(ForumDetail, self).get_context_data(**kwargs)
        ctx['komentar'] = Komentar.objects.all().filter(forum_id=ctx['forum_detail'].pk)
        # print(ctx['forum_detail'].pk)
        return ctx



