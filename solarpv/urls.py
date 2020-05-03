from django.urls import path, include
from django.contrib.auth.views import LoginView
from django_registration.backends.one_step.views import RegistrationView
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    #path('login/', LoginView.as_view(), name='login'),
    path('login/', views.user_login, name='login'),
]
