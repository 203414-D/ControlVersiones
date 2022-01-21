from django.urls import path, re_path

#importacion de vistas
from primerComponente.views import PrimerViewList

urlpatterns = [
    re_path(r'^lista/$', PrimerViewList.as_view()),    
]