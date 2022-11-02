from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=50) # CharField for a small string
    description = models.TextField() # TextField for a large text field
    # ID field is automatically created by Django
