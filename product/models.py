from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    product_name=models.CharField(max_length=200)
    product_price=models.CharField(max_length=200)
    product_image=models.FileField(upload_to="product_images/")

    class Meta:
        db_table="product"



class Orders(models.Model):
    STATUS = (
        ('Ordered', 'Ordered'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=STATUS, default='Ordered')