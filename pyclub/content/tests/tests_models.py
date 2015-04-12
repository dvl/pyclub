# -*- coding: utf-8 -*-

from itertools import cycle

from django.test import TestCase

from model_mommy.recipe import Recipe

from .. import models


class PostTestCase(TestCase):

    def setUp(self):
        post_recipe = Recipe(models.Post, status=cycle([models.Post.DRAFT, models.Post.FINISHED]))
        post_recipe.make(_quantity=10)

    def test_queryset_should_contain_only_finished_entries(self):
        posts = models.Post.objects.finished()

        self.assertEqual(posts.count(), 5)
        self.assertTrue(all(p.status == models.Post.FINISHED for p in posts))

    def test_queryset_should_contains_only_draft_entries(self):
        posts = models.Post.objects.draft()

        self.assertEqual(posts.count(), 5)
        self.assertTrue(all(p.status == models.Post.DRAFT for p in posts))
