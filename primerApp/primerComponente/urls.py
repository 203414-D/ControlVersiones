from django.urls import path, re_path

#importacion de vistas
from primerComponente.views import PrimerViewList
from primerComponente.views import PrimerViewDetail

urlpatterns = [
    re_path(r'^v1/lista/$', PrimerViewList.as_view()),
    re_path(r'^v2/lista/(?P<pk>\d+)$', PrimerViewDetail.as_view()),    
]