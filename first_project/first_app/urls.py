from django.conf.urls import url 
from first_app import views 
from django.urls import path
 
urlpatterns = [ 
    # url(r'^api/instrumento$', views.add_instrumento),
    # url(r'^api/first_app/published$', views.first_app_list_published),
    # url(r'^api/first_app/teste$', views.index)
    # url(r'^api/add_instrumento$', views.add_instrumento),
    url(r'^api/get_instrumentos$', views.get_instrumentos),
    url(r'^api/gerar_dados_tweets$', views.gerar_dados_tweets),
    url(r'^api/gerar_cupoms$', views.gerar_cupoms),
    url(r'^api/add_usuario$', views.add_usuario),
    url(r'^api/add_evento$', views.add_evento),
    url(r'^api/add_contrato$', views.add_contrato),
    url(r'^api/get_generos_banda_artista$', views.get_generos_banda_artista),
    path('api/get_banda_artista/<int:pk>', views.get_banda_artista),
]