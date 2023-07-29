from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('mobile-home.html', views.mobile_home, name='mobile_home'),
    path('mobile_redirect/', views.mobile_redirect, name='mobile_redirect'),
    path('careers/', views.careers, name='careers'),
    path('returns/', views.returns, name='returns'),
    path('terms/', views.terms, name='terms'),
]
