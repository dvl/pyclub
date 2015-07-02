# -*- coding: utf-8 -*-

from django.test import TestCase

from model_mommy import mommy

from .models import User


class TestUserModel(TestCase):
    def test_display_name(self):
        user1 = mommy.make(User, first_name='foo', last_name='bar')
        self.assertEqual(user1.display_name(), 'foo bar')

        user2 = mommy.make(User, first_name='', last_name='', username='foobar')
        self.assertEqual(user2.display_name(), 'foobar')
