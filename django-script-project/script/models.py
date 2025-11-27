from django.db import models
from django import forms

# Create your models here.

class CategoryGroup(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Script(models.Model):
    CategoryGroup = models.ForeignKey(CategoryGroup, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    content = models.CharField(max_length=1000)

    def __str__(self):
        complete_script = self.name + ' ' + self.content
        return complete_script
