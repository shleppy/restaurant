from django.db import models


# Create your models here.
class Category(models.Model):
    """Item category"""
    name = models.CharField(max_length=15)
    description = models.TextField(max_length=50)
    CATEGORY_TYPE = [
        (0, 'STARTER'),
        (1, 'MAIN COURSE'),
        (2, 'DESSERT'),
        (3, 'BEVERAGE'),
        (4, 'ADDITION')
    ]
    type = models.CharField(max_length=1, choices=CATEGORY_TYPE, default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"


class Item(models.Model):
    """Item """
    name = models.CharField(max_length=15)
    price = models.IntegerField()
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name + ", cat = " + str(self.category) + ", price = " + str(self.price) + " cents"


class Customer(models.Model):
    """Customer model where every Customer is treated as a unique customer."""
    name = models.CharField(max_length=15)
    date = models.DateTimeField()
    items = []

    def __str__(self):
        return self.name + str(self.date)


