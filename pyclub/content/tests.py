# -*- coding: utf-8 -*-

from itertools import cycle

from django.test import TestCase

from model_mommy.recipe import Recipe

from . import models, choices


class PostTestCase(TestCase):

    def setUp(self):
        post_recipe = Recipe(models.Post, status=cycle([choices.DRAFT, choices.FINISHED]))
        post_recipe.make(_quantity=10)

    def test_queryset_should_contain_only_finished_entries(self):
        posts = models.Post.objects.finished()

        self.assertTrue(all(p.status == choices.FINISHED for p in posts))

    def test_queryset_should_contains_only_draft_entries(self):
        posts = models.Post.objects.draft()

        self.assertTrue(all(p.status == choices.DRAFT for p in posts))
