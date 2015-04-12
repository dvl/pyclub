# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.test import TestCase

from model_mommy.recipe import Recipe

from .. import models


class PostListViewTestCase(TestCase):

    def test_post_with_single_revision(self):
        res = self.client.get(reverse('content:list'))

        self.assertEqual(res.status_code, 200)

