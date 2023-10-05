from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.


def Home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        return redirect('login')
