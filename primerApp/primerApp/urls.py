
import django
from django.urls import path, include, re_path 
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
     path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
     re_path(r'^api/', include('Login.urls')),
     re_path(r'^api/', include('primerComponente.urls')),
     re_path(r'^api/',  include('Register.urls')),
     re_path(r'^api/v1/loadImage/', include('loadImage.urls')),
     re_path(r'^api/', include('UserProfile.urls')),
     re_path(r'assets/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),

] 
