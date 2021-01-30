from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('show',views.show),
    path('add',views.add),  
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy), 
]