from . import views
from django.urls import path


urlpatterns = [
    path('', views.login, name = 'login'),
    path('login', views.login, name = 'login'),
    path('checklogin', views.checklogincredentials, name = 'checklogin'),
    path('signup', views.signuprequest, name = 'signup'),
    path('signuppage', views.signuppage, name = 'signuppage'),
    path('process_form', views.process_form, name = 'process_form')
]