from django.db import models, transaction

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    stock_quantity = models.PositiveIntegerField(default=0)
    image_url = models.URLField(max_length=500, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def reduce_stock(self, quantity):
        with transaction.atomic():
            product = Product.objects.select_for_update().get(id=self.id)
            if product.stock_quantity >= quantity:
                product.stock_quantity -= quantity
                product.save()
            else:
                raise ValueError('Insufficient stock')

class InsufficientStockError(Exception):
    pass

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        try:
            self.product.reduce_stock(self.quantity)
        except ValueError:
            raise InsufficientStockError('Not enough stock for this order')
        
        super().save(*args, **kwargs)

