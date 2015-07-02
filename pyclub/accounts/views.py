# -*- coding: utf-8 -*-

from django.views import generic

from braces import views as braces


class LinkedAccountsView(braces.LoginRequiredMixin, generic.TemplateView):
    template_name = 'accounts/linked_accounts.html'
