# -*- coding: utf-8 -*-

from django.db import models
from diario.models import Diario
from django.contrib.auth.models import User

class PortadaBase(models.Model):
    codigo = models.AutoField(primary_key=True,
    db_index=True)
    fec_creacion = models.DateField(verbose_name=u'Fecha de diarios', unique=True)

    def __unicode__(self):
        return u'Portadas de diarios del día %s' % self.fec_creacion

    class Meta:
        verbose_name = u'Portada de diario'
        verbose_name_plural = u'Portadas de diarios'

class Portada(models.Model):
    codigo = models.AutoField(primary_key=True,
	db_index=True)
    imagen = models.ImageField(upload_to='portadas/%Y/%m/%d')
    diario = models.ForeignKey(Diario)
    orden = models.PositiveSmallIntegerField(default=0)
    portada = models.ForeignKey(PortadaBase)
    fec_creacion = models.DateTimeField(auto_now_add=True,
	editable=False,null=True,blank=True,)
    usu_creacion = models.ForeignKey(User,
	editable=False,null=True,blank=True,
	related_name='portadas_creadas')
    fec_modificacion = models.DateTimeField(null=True,
    blank=True,
	editable=False)
    usu_modificacion = models.ForeignKey(User,
	editable=False,null=True,blank=True,
	related_name='portadas_modificadas')
    
    def __unicode__(self):
    	return u'%s' % self.diario

    class Meta:
        ordering = ['orden',]
        unique_together = ('portada','diario',)
        verbose_name = u'Portada de diario'
        verbose_name_plural = u'Portadas de diarios'
