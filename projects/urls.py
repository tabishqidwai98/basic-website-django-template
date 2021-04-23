from django.urls import path, include
from .views import homeview,termsview,orderview,dashboardview

urlpatterns = [
    path('',homeview,name='home'),
    path('terms',termsview,name='terms'),
    path('order',orderview,name='order'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('dashboard/',dashboardview,name='dashboard'),
    path('register',register, name='register'),
]