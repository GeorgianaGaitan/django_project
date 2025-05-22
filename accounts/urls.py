from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
   # path('logout/', views.logout_view, name='logout'),
    path('home/', views.home_view, name='home'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')

]
