# -*- coding: utf-8 -*-

from django.views import generic

from . import models


class PostListView(generic.ListView):
    ordering = ('-created_at',)
    paginate_by = 5
    queryset = models.Post.objects.approved_posts().finished()
