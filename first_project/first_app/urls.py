from django.conf.urls import url 
from first_app import views 
 
urlpatterns = [ 
    # url(r'^api/instrumento$', views.add_instrumento),
    # url(r'^api/first_app/published$', views.first_app_list_published),
    # url(r'^api/first_app/teste$', views.index)
    # url(r'^api/add_instrumento$', views.add_instrumento),
    url(r'^api/get_instrumentos$', views.get_instrumentos),
]