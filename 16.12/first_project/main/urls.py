from django.urls import path
from . import views

urlpatterns = [
    path("", views.song_en, name="song_en"),     
    path("fr/", views.song_fr, name="song_fr"),  
    path("de/", views.song_de, name="song_de"),  
    path("es/", views.song_es, name="song_es"),  
    path("cars/", views.cars_home, name="cars_home"),
    path("cars/toyota/", views.cars_toyota, name="cars_toyota"),
    path("cars/honda/", views.cars_honda, name="cars_honda"),
    path("cars/renault/", views.cars_renault, name="cars_renault"),
    path("weekday/", views.weekday, name="weekday"),
    path("headphones/", views.headphones, name="headphones"),
]
