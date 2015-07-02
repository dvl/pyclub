# -*- coding: utf-8 -*-

from django.test import TestCase


class TestContextProcessor(TestCase):
    def test_site_info_is_setted(self):
        response = self.client.get('/')

        self.assertTrue('SITE_NAME' in response.context)
        self.assertTrue('TAG_LINE' in response.context)
