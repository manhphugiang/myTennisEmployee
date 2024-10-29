from django.urls import path
from . import views

urlpatterns= [
    path('', views.main, name='mainIndex'),

    path('members/', views.members, name='members'),

    path('members/details/<int:id>', views.details),
    path('testing/', views.testing, name='testing'),    
]