# -*- coding: utf-8 -*-

from django.views import generic

from . import models


class PostListView(generic.ListView):
    queryset = models.Post.objects.posts().finished()
    ordering = ('-created_at',)
    paginate_by = 5
