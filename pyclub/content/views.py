# -*- coding: utf-8 -*-

from django.db.models import Max, F, Q
from django.views import generic

from . import models


class PostListView(generic.ListView):

    def get_queryset(self):
        # isso pode ficar no queryset manager?
        return (
            models.Post.objects
            .annotate(
                last_created=Max('revision__created_at')
            )
            .filter(
                Q(revision__created_at=F('last_created')) &
                Q(revision__approved_author=True) &
                Q(revision__approved_staff=True)
            )
            .finished()
        )
