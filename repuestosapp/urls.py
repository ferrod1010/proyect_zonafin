from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^vehiculo/nuevo/$', views.vehiculo_nuevo, name='vehiculo_nuevo'),
    ]
