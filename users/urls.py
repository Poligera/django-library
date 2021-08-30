from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.login_request, name="login"),
    path('logout/', views.logout_request, name="logout")
]