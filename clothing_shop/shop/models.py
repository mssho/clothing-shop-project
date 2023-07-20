from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50)

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    discription = models.TextField()
    price = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_images = models.URLField()


