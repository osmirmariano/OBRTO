
from django.conf.urls import url
from noticias import views

urlpatterns = [
    url(r'^$', views.ListarNoticia.as_view(), name='listar-noticias'),
    url(r'adicionar$', views.AdicionarNoticia.as_view(), name='adicionar-noticias'),
    url(r'^excluir/(?P<pk>[0-9]+)/$', views.DeletarNoticia.as_view(), name='deletar-noticias'),
    url(r'^(?P<pk>[0-9]+)/$', views.EditarNoticia.as_view(), name='editar-noticias'),
    url(r'^visualizar/(?P<pk>[0-9]+)/$', views.VisualizarNoticia.as_view(), name='visualizar-noticias'),
]