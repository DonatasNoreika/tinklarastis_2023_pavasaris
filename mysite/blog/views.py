from django.shortcuts import render
from django.views import generic
from .models import Post, Comment
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class PostListView(generic.ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    fields = ['title', 'text']
    success_url = '/'
    template_name = 'post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
