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
    def __init__(self, *args, **kwargs):
        super(FormularioNoticia, self). __init__(*args, **kwargs)
        
        self.fields['titulo'].label = 'Título:'
        self.fields['titulo'].widget.attrs['class'] = 'validate'
        self.fields['titulo'].widget.attrs['placeholder'] = 'Título da notícia...'
        self.fields['titulo'].widget.attrs['required'] = 'required'
        
        self.fields['resumo'].label = 'Resumo:'
        self.fields['resumo'].widget.attrs['class'] = 'validate'
        self.fields['resumo'].widget.attrs['placeholder'] = 'Resumo da notícia...'
        self.fields['resumo'].widget.attrs['required'] = 'required'

        self.fields['descricao'].label = 'Descrição:'
        self.fields['descricao'].widget.attrs['class'] = 'materialize-textarea'
        self.fields['descricao'].widget.attrs['placeholder'] = 'Descrição da notíca...'
        self.fields['descricao'].widget.attrs['required'] = 'required'

        self.fields['image'].label = 'Upload de Imagem:'
        self.fields['image'].widget.attrs['required'] = 'required'
        
        