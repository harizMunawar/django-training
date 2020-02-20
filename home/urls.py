from django.urls import path, re_path
from . import views
from .models import menu

data = menu.objects.all()

urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact),
    path('detail/', views.detail),
    re_path(r'^(?P<inputSlug>[\w-]+)/$', views.menumartabak),
]