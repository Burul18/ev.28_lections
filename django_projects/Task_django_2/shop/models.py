from django.db import models


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


# Product.objects.filter(category=1)