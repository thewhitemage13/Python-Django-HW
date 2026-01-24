from django.urls import path
from . import views

urlpatterns = [
    path('', views.restaurant_list, name='restaurant_list'),
    path('create/', views.restaurant_create, name='restaurant_create'),
    path('<int:pk>/edit/', views.restaurant_update, name='restaurant_update'),
    path('<int:pk>/delete/', views.restaurant_delete, name='restaurant_delete'),
]
