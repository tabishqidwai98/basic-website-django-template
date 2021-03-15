from django.urls import path
from .views import homeview,termsview,orderview,signupview,loginview

urlpatterns = [
    path('',homeview,name='home'),
    path('terms',termsview,name='terms'),
    path('order',orderview,name='order'),
    path('signup',signupview,name='signup'),
    path('login',loginview,name='login'),
]