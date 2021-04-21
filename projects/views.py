from django.shortcuts import render

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
