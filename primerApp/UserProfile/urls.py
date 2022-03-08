from ast import Import
from django.urls import path, re_path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

from UserProfile.views import ProfileList, ProfileTablaDetail

urlpatterns = [
    re_path(r'^v1/user/$', ProfileList.as_view()),
    re_path(r'^v2/user/(?P<pk>\d+)$', ProfileTablaDetail.as_view()),
] + static(settings.MEDIA_URL, document_rot=settings.MEDIA_ROOT)