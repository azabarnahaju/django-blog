from django.shortcuts import render, get_object_or_404
from datetime import date
from .models import Post
from django.views.generic import ListView, DetailView


# Create your views here.


class IndexView(ListView):
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    model = Post
    ordering = ["-date"]

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset[:3]


class PostsView(ListView):
    template_name = 'blog/all-posts.html'
    context_object_name = 'posts'
    ordering = ["-date"]
    model = Post


class PostDetailView(DetailView):
    template_name = "blog/post-detail.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_tags"] = self.object.tags.all()
        return context

