from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('router/', views.RouterView.as_view()),
    path('router/<int:pk>', views.RouterView.as_view()),
    path('router/<str:ip>', views.RouterView.as_view()),
]