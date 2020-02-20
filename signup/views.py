from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def index(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserCreationForm()    
    return render(request, 'signup/index.html', {'form' : form})