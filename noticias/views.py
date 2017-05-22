# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from noticias.models import Noticia
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from noticias.forms import *
from django.contrib.auth import authenticate,logout 
from django.shortcuts import render, redirect
from django.http.response import HttpResponseRedirect
from django.views.generic import View
from django.shortcuts import render

class ListarNoticia(LoginRequiredMixin, ListView):
    """
    Formulario para listas as noticas adicionadas
    """
    
    login_url = '/'
    model = Noticia
    template_name = 'index.html'

    #def get_queryset(self):
        #queryset = Tarefas.objects.filter(dono=self.request.user)
        #return queryset



class AdicionarNoticia(LoginRequiredMixin, CreateView):
    login_url = '/'
    model = Noticia
    form_class = FormularioNoticia
    template_name = 'noticias/adicionar.html'
    success_url = reverse_lazy('listar-tarefas')