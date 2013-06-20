# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html
from sorl.thumbnail import get_thumbnail

class Diario(models.Model):
    codigo = models.AutoField(primary_key=True,
	db_index=True)
    nombre = models.CharField(max_length=70,
	db_index=True)
    url = models.URLField(null=True,blank=True)
    imagen = models.ImageField(upload_to='diario',
    	null=True,blank=True)
    fec_creacion = models.DateTimeField(auto_now_add=True,
    editable=False,null=True,blank=True,)
    usu_creacion = models.ForeignKey(User,
    editable=False,null=True,blank=True,
    related_name='diarios_creados')
    fec_modificacion = models.DateTimeField(null=True,
    blank=True,
    editable=False)
    usu_modificacion = models.ForeignKey(User,
    editable=False,null=True,blank=True,
    related_name='diarios_modificados')

    def __unicode__(self):
    	return u'%s' % self.nombre

    def imagen_ashtml(self):
        if self.imagen:
            thumb = get_thumbnail(self.imagen,'80x54', quality=99)
            return format_html('<img src="{0}" />',
            thumb.url)
        return 'Sin Imagen'
    imagen_ashtml.allow_tags = True
    imagen_ashtml.short_description = u'Imagen'

    def url_ashtml(self):
        if self.url:
            return format_html('<a href="{0}" target="_blank">{0}</a>',self.url)
        return u'Sin web site'
    url_ashtml.allow_tags = True
    url_ashtml.short_description = u'Web Site'

    class Meta:
        verbose_name = u'Diario'
        verbose_name_plural = u'Diarios'
        ordering = ['codigo',]
