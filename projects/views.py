from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse
from .forms import CoustomUserCreationForm

# Create your views here.

def homeview(request):
    return render(request, 'index.html')

def termsview(request):
    return render(request, 'terms.html')

def orderview(request):
    context = {}
    return render(request, 'order.html', context)

def dashboardview(request):
    return render(request, 'users/dashboard.html')

def register(request):
    if request.method == 'GET':
        return render(request, 'users/register.html',{'form': CoustomUserCreationForm})
    elif request.method == 'POST':
        form = CoustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.backend = "django.contrib.auth.backends.ModelBackend"
            user.save()
            login(request, user)
            return redirect(reverse('dashboard'))
