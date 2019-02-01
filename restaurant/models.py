from django.db import models

# Create your models here.


class Customer(models.Model):
    """Customer model where every Customer is treated as a unique customer."""
    name = models.CharField(max_length=15)
    date = models.DateTimeField()
