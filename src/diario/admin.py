# -*- coding: utf-8 -*-

from django.contrib import admin
from django.db import models

from .models import Diario


class DiarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'url_ashtml', 'imagen_ashtml')
    

admin.site.register(Diario, DiarioAdmin)