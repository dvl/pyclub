# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect
from django.views import generic
from braces import views as braces

from . import forms, models


class PostListView(generic.ListView):
    model = models.Post


class PostDetailView(generic.DetailView):
    model = models.Post


class PostCreateView(braces.LoginRequiredMixin, generic.CreateView):
    model = models.Post
    form_class = forms.PostForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())


class PostUpdateView(braces.LoginRequiredMixin, generic.UpdateView):
    pass
