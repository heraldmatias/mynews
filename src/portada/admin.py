# -*- coding: utf-8 -*-

from django.contrib import admin
from django.db import models
from django import forms

from .models import Portada, PortadaBase

class PortadaInline(admin.TabularInline):
    model = Portada
    extra = 1


class PortadaBaseAdmin(admin.ModelAdmin):
    inlines = [
        PortadaInline,
    ]

admin.site.register(PortadaBase, PortadaBaseAdmin)