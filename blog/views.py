from django.shortcuts import render, get_object_or_404
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 3


class UserPostListView(LoginRequiredMixin, ListView):
    model = Post

    template_name = 'blog/userPosts.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

    def get_queryset(self):
        user = get_object_or_404(User, username = self.kwargs.get('username'))
        return Post.objects.filter(author = user)


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post

    template_name = 'blog/detail.html'    


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post

    template_name = 'blog/create.html'
    fields = [
        'title',
        'content'
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post

    template_name = 'blog/create.html'
    fields = [
        'title',
        'content'
    ]

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    
    template_name = 'blog/delete.html'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


@login_required
def about(request):
    url = 'blog/about.html'
    context = {}
    return render(request, url, context)