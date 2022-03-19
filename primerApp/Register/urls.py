from django.urls import re_path
from Register.views import RegisterUser, RegisterUserNew, RegisterN

urlpatterns = [
     re_path(r'^v1/register', RegisterUser.as_view()),
     re_path(r'^v2/register', RegisterUserNew.as_view()),
     re_path(r'^v1/upd/(?P<pk>\d+)$', RegisterN.as_view()),
]
   
