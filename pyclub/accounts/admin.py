# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from . import forms


@admin.register(get_user_model())
class UsuarioAdmin(UserAdmin):
    add_form = forms.UserCreationForm
