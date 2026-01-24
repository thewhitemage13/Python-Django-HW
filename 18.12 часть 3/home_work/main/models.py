from django.db import models

class Book(models.Model):
    title = models.CharField("Назва книги", max_length=200)
    author = models.CharField("Автор", max_length=150)
    year = models.PositiveIntegerField("Рік видання")
    style = models.CharField("Стиль", max_length=80)
    publisher = models.CharField("Видавництво", max_length=120)
    is_available = models.BooleanField("Є в наявності", default=True)

    def __str__(self) -> str:
        return f"{self.title} — {self.author}"


class Reader(models.Model):
    first_name = models.CharField("Ім'я", max_length=50)
    last_name = models.CharField("Прізвище", max_length=50)
    phone = models.CharField("Контактний телефон", max_length=20)
    email = models.EmailField("Email", unique=True)
    joined_at = models.DateField("Дата запису до бібліотеки", auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"