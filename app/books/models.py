from django.db import models

# Abstract class to define general attributes of a book


class AbstractBook(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        abstract = True

# Child class inheriting from AbstractBook


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(AbstractBook):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, blank=True)
    is_on_sale = models.BooleanField(default=False)
    discount_percentage = models.DecimalField(
        max_digits=5, decimal_places=2, default=0.0)

    def discounted_price(self):
        if self.is_on_sale:
            return self.price - (self.price * self.discount_percentage / 100)
        return self.price

    def __str__(self):
        return self.title
