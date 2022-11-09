from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Movie(models.Model):
    movie = models.CharField(max_length=100)
    time = models.TimeField()
    price = models.DecimalField(max_digits=10, decimal_places=3)
    watchers = models.PositiveIntegerField()

    def __str__(self):
        return f"for {self.watchers} at {self.time}"

