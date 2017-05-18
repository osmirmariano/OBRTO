
from django.conf.urls import url
from noticias import views

urlpatterns = [
    url(r'^$', views.ListarNoticia.as_view(), name='listar-noticias'),
    url(r'adicionar$', views.AdicionarNoticia.as_view(), name='adicionar-noticias'),
]