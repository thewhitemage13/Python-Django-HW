from django.urls import path
from . import views

app_name = "hw_forms"

urlpatterns = [
    path("task1/", views.task1_login, name="task1"),
    path("task2/", views.task2_three_numbers, name="task2"),
    path("task3/", views.task3_shop_register, name="task3"),
    path("task4/", views.task4_programmer_day, name="task4"),
]
