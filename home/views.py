from django.shortcuts import render
from .models import menu

def index(request):
    Menu = menu.objects.all()
    context = {
        'nav' : [
            ['contact/', 'Contact'],
            ['detail/', 'Detail'],
        ],
        'Menu' : Menu,
    }
    return render(request, 'home/index.html', context)

def contact(request):
    context = {
        'judul' : 'Contact',
        'linkImage' : 'home/img/banner_contact.png',
        'linkCSS' : 'home/css/style.css',
    }
    return render(request, 'home/navbarURL.html', context)

def detail(request):
    context = {
        'judul' : 'Detail',
        'linkImage' : 'home/img/banner_detail.png',
        'linkCSS' : 'home/css/style.css',
    }
    return render(request, 'home/navbarURL.html', context)