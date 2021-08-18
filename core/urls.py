from django.urls import path
from . import views
urlpatterns = [
    path('', views.inicio),
    path('show_index', views.index),
    path('autor/', views.autor),
    path('libro/', views.libro),
    path('ninja/', views.ninja),
]
