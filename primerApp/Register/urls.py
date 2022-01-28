from django.urls import re_path
from Register.views import RegisterUser

urlpatterns = [
     re_path(r'^', RegisterUser.as_view()),
]
   
