from django.db import models
from django.utils import timezone


class Reader(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    phone = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    joined_at = models.DateField(default=timezone.now)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=150)
    publish_year = models.PositiveIntegerField()
    style = models.CharField(max_length=100)      
    publisher = models.CharField(max_length=150)

    def __str__(self) -> str:
        return f"{self.title} — {self.author}"

    @property
    def is_available(self) -> bool:
        return not self.borrows.filter(returned_at__isnull=True).exists()


class Borrow(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="borrows")
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE, related_name="borrows")
    borrowed_at = models.DateField(default=timezone.now)
    returned_at = models.DateField(null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["book"],
                condition=models.Q(returned_at__isnull=True),
                name="unique_active_borrow_per_book",
            )
        ]

    def __str__(self) -> str:
        return f"{self.book} -> {self.reader}"
