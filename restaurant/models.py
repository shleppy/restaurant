from django.db import models


# Create your models here.
class Category(models.Model):
    """Item category"""
    name = models.CharField(max_length=15, db_index=True)
    description = models.TextField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True)
    CATEGORY_TYPE = [
        (0, 'STARTER'),
        (1, 'MAIN COURSE'),
        (2, 'DESSERT'),
        (3, 'BEVERAGE'),
        (4, 'ADDITION')
    ]
    type = models.IntegerField(choices=CATEGORY_TYPE, default=1)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('type',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class Item(models.Model):
    """Item """
    name = models.CharField(max_length=15, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    price = models.DecimalField(decimal_places=2, max_digits=100)
    description = models.TextField()
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name + ", cat = " + str(self.category) + ", price = " + str(self.price) + " cents"

    class Meta:
        ordering = ('name',)


class Customer(models.Model):
    """Customer model where every Customer is treated as a unique customer."""
    name = models.CharField(max_length=15)
    date = models.DateTimeField()
    items = []

    def __str__(self):
        return self.name + str(self.date)


