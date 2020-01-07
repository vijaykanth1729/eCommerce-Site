from django.db import models
from django.urls import reverse


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10,default=25.89)
    sale_price = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ('title','slug')

    def get_absolute_url(self):
        return reverse('products:detail', kwargs={'slug':self.slug})


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/images/')
    thumbnail = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.product.title


