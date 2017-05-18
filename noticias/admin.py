# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import *

#class NoticiaAdmin(admin.ModelAdmin):
#    list_display = ['titulo', 'resumo', 'descricao', 'imagem']
admin.site.register(Noticia)