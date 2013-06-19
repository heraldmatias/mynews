# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

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

    class Meta:
        verbose_name = u'Diario'
        verbose_name_plural = u'Diarios'
        ordering = ['codigo',]
