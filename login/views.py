from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout as out
from django.contrib.auth.models import User

def index(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            loginguest = form.get_user()
            user = User.objects.get(username = loginguest.username)
            login(request, loginguest)
            if user.is_superuser == 1:
                return redirect('/admin/')
            else:
                return redirect('/home/')
    else:
        form = AuthenticationForm()
    return render(request, 'login/index.html', {'form' : form})