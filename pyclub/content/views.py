# -*- coding: utf-8 -*-

from django.views import generic
from braces import views as braces

from . import forms, models


class PostCreateView(braces.LoginRequiredMixin, generic.CreateView):
    model = models.Post
    form_class = forms.PostForm


class PostUpdateView(braces.LoginRequiredMixin, generic.UpdateView):
    pass
