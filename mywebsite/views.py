from django.shortcuts import render
from django.contrib.auth import logout

def index(request):
    if request.method == 'POST':
        logout(request)
    return render(request, 'index.html')