from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('api-auth/', include('rest_framework.urls')),
    path('home/', include('home.urls')),
    path('login/', include('login.urls'), name="login"),
    path('signup/', include('signup.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)