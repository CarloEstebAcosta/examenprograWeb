#esta la cree ----

from django.urls import path
from  . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('crud', views.crud, name='crud'),
    path('Nosotros', views.Nosotros, name='Nosotros'),
    path('Contacto', views.Contacto, name='Contacto'),
    path('Fundaciones', views.Fundaciones, name='Fundaciones'),
    path('Tienda', views.Tienda, name='Tienda'),
    path('AcsTienda', views.AcsTienda, name='AcsTienda'),
    path('AliTienda', views.AliTienda, name='AliTienda'),

]