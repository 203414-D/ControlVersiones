from django.urls import re_path
from Register.views import RegisterUser, RegisterUserNew

urlpatterns = [
     re_path(r'^v1/register', RegisterUser.as_view()),
     re_path(r'^v2/register', RegisterUserNew.as_view()),
]
   
