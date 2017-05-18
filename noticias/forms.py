# -*- coding: utf-8 -*-
from django import forms
from noticias.models import *

class FormularioNoticia(forms.ModelForm):
    """
    Formulario para o model Tarefas
    """
    class Meta:
        model = Noticia
        exclude = []