# -*- coding: utf-8 -*-

from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views import generic

from braces import views as braces

from .forms import PostForm
from .models import Post


class PostListView(generic.ListView):
    model = Post
    queryset = Post.objects.live()


class PostDetailView(generic.DetailView):
    model = Post

    def get_queryset(self):
        return self.model.objects.filter(
            (Q(status=Post.FINISHED) & Q(approved=True)) |
            Q(created_by=self.request.user)
        )


class PostCreateView(braces.LoginRequiredMixin, generic.CreateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())


class PostUpdateView(braces.LoginRequiredMixin, generic.UpdateView):
    model = Post
    form_class = PostForm

    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg, None)

        if not queryset:
            queryset = self.get_queryset()

        if not self.request.user.is_superuser:
            queryset = queryset.filter(created_by=self.request.user)

        return get_object_or_404(queryset, pk=pk)
