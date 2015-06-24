# -*- coding: utf-8 -*-

from django.views import generic
from braces import views as braces


class IndexView(braces.LoginRequiredMixin, generic.TemplateView):
    template_name = 'dashboard/index.html'
