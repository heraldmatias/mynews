# -*- coding: utf-8 -*-

from django.contrib import admin
from django.db import models

from .models import Diario


class DiarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'url', 'imagen',)
    

admin.site.register(Diario, DiarioAdmin)