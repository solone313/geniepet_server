from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views
from django.conf.urls import include, url

urlpatterns = [
    path('kakaopay/', views.kakaoPay),
    path('approve/', views.payapporve),
    path('success/', views.success),
    path('pay/',views.pay)
	]