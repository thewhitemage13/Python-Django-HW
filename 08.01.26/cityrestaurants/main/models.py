from django.db import models

# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    specialization = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    website = models.URLField(blank=True)
    phone = models.CharField(max_length=50)

    def __str__(self):
        return self.name