from django.db import models

# Create your models here.

class Calification(models.Model):
    name = models.CharField(max_length=100)
    comment = models.TextField()
    rating = models.IntegerField()
    calification_date = models.DateField()