from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User

from . import views


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls), name="index"),
    path('api-auth/', include('rest_framework.urls')),
    path('home/', include('home.urls')),
    path('login/', include('login.urls'), name="login"),
    path('signup/', include('signup.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)