from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import menu

@login_required
def index(request):
    Menu = menu.objects.all()
    paginator = Paginator(Menu, 4)
    page = request.GET.get('page', 1)

    pagination = paginator.page(page)
    context = {
        'nav' : [
            ['contact/', 'Contact'],
            ['detail/', 'Detail'],
        ],
        'Menu' : Menu,
        'pagination' : pagination,
        'page' : page,
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