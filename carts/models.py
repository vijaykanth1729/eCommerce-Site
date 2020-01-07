from django.db import models
from products.models  import  Product
class Cart(models.Model):
    products = models.ManyToManyField(Product)
    total = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return f"Cart id: {self.id}"




