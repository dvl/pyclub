# -*- coding: utf-8 -*-

from itertools import cycle

from django.test import TestCase

from model_mommy.recipe import Recipe

from .models import Post


class TestPostModel(TestCase):
    def setUp(self):
        self.recipe = Recipe(Post, slug=None)

    def test_str(self):
        post = self.recipe.make(title='foobar')
        self.assertEqual(post.__str__(), 'foobar')

    def test_get_absolute_url(self):
        post = self.recipe.make(title='foobar')
        self.assertEqual(post.get_absolute_url(), '/foobar/')

    def test_queryset(self):
        # cria 2 posts
        self.recipe.make(status=cycle([Post.FINISHED, Post.DRAFT]), _quantity=2)

        # Aprova os finalizados
        Post.objects.filter(status=Post.FINISHED).update(approved=True)

        # cria mais 2 posts para termos finalizados não aprovados
        self.recipe.make(status=cycle([Post.FINISHED, Post.DRAFT]), _quantity=2)

        self.assertEqual(Post.objects.finished().count(), 2)
        self.assertEqual(Post.objects.draft().count(), 2)
        self.assertEqual(Post.objects.approved().count(), 1)
        self.assertEqual(Post.objects.live().count(), 1)



