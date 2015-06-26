# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext as _

from . import forms


@admin.register(get_user_model())
class UsuarioAdmin(UserAdmin):
    add_form = forms.UserCreationForm

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email',
                                         'about')}),
        (_('Social'), {'fields': ('github', 'bitbucket', 'gitlab',  'twitter',
                                  'facebook', 'linkedin', 'gratipay')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
