from django.urls import path, re_path

from loadImage.views import ImagenView
from loadImage.views import ImagenViewDetail

urlpatterns = [
    re_path(r'^listaImagen/$', ImagenView.as_view()),
    re_path(r'listaImagen/(?P<pk>\d+)$', ImagenViewDetail.as_view())
    
]