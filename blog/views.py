from django.shortcuts import render, get_object_or_404
from datetime import datetime
from .models import Post
from django.views.generic import ListView, DetailView
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import CommentForm

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


class PostDetailView(View):
    def is_stored_post(self, req, post_id):
        stored_posts = req.session.get('stored_posts')
        if stored_posts is not None:
            is_saved_for_later = post_id in stored_posts
        else:
            is_saved_for_later = False
        return is_saved_for_later

    def get(self, req, slug):
        post = Post.objects.get(slug=slug)
        context = {
            'post': post,
            "post_tags": post.tags.all(),
            'comment_form': CommentForm(),
            'comments': post.comments.all().order_by('-date'),
            'is_saved_for_later': self.is_stored_post(req, post.id),
        }
        return render(req, "blog/post-detail.html", context)

    def post(self, req, slug):
        comment_form = CommentForm(req.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.date = datetime.now()
            comment.save()
            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))

        context = {
            'post': post,
            "post_tags": post.tags.all(),
            'comment_form': comment_form,
            'comments': post.comments.all().order_by('-date'),
            'is_saved_for_later': self.is_stored_post(req, post.id),
        }

        return render(req, "blog/post-detail.html", context)


class ReadLaterView(View):
    def get(self, req):
        stored_posts = req.session.get('stored_posts')

        context = {}

        if stored_posts is None or len(stored_posts) == 0:
            context["posts"] = []
            context["has_posts"] = False
        else:
            posts = Post.objects.filter(id__in=stored_posts)
            context["posts"] = posts
            context["has_posts"] = True

        return render(req, "blog/stored-posts.html", context)

    def post(self, req):
        stored_posts = req.session.get("stored_posts")
        if stored_posts is None:
            stored_posts = []

        post_id = int(req.POST["post_id"])

        if post_id not in stored_posts:
            stored_posts.append(post_id)
        else:
            stored_posts.remove(post_id)

        req.session["stored_posts"] = stored_posts
        return HttpResponseRedirect("/")
