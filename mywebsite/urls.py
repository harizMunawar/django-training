from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('home/', include('home.urls')),
    path('login/', include('login.urls'), name="login"),
    path('signup/', include('signup.urls')),
    path('ratings/', include('star_ratings.urls', namespace='ratings', app_name='ratings')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)