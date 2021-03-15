from django.shortcuts import render

# Create your views here.

def homeview(request):
    context = {}
    return render(request, 'index.html', context)

def termsview(request):
    context = {}
    return render(request, 'terms.html', context)

def orderview(request):
    context = {}
    return render(request, 'order.html', context)

def signupview(request):
    context = {}
    return render(request, 'signup.html', context)

def loginview(request):
    context = {}
    return render(request, 'login.html', context)