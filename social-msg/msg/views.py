from django.views.generic import ListView, DetailView

from . models import Post


class MsgListView(ListView):
    model = Post
    template_name = 'home.html'


class MsgDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
