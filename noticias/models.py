
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Noticia(models.Model):

    titulo = models.CharField(max_length=255)
    resumo = models.CharField(max_length=255)
    descricao = models.TextField()
    image = models.ImageField('Imagem',upload_to='noticia', blank=True)

    def __unicode__(self):
        return '{0} - {1} - {2} - {3} - {4}'.format(
            self.titulo,
            self.resumo,
            self.descricao,
            self.image
        )