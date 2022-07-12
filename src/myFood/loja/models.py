from django.conf import settings
from django.db import models


# Create your models here.

class Banner(models.Model):
    img = models.CharField(max_length=200)
    alt_text = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'


class Category(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category', blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'category'

class Cat(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category', blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'cat'


class Marca(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Size(models.Model):
    title = models.CharField(max_length=100,)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'size'

#Product
class Product(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=400)
    image = models.ImageField(upload_to='product', blank=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'product'


class ProductAttribute(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.product.title

    class Meta:
        db_table = 'product_attribute'



#Cart 
User = settings.AUTH_USER_MODEL
class Cart(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.id)



class Order(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.title

    class Meta:
        db_table = 'order'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.product.title

    class Meta:
        db_table = 'order_item'


class OrderItemAttribute(models.Model):
    order_item = models.ForeignKey(OrderItem, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'order_item_attribute'
