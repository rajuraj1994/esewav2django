from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    category_name=models.CharField(max_length=255,unique=True)
    created_at=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_name=models.CharField(max_length=255)
    product_price=models.FloatField()
    stock=models.IntegerField()
    product_description=models.TextField()
    product_image=models.FileField(upload_to='static/uploads',null=True)
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.product_name

class Cart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True,null=True)

class Order(models.Model):
    PAYMENT=(
        ('Cash on Delivery','Cash on Delivery'),
        ('Esewa','Esewa')
    )
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    total_price=models.IntegerField()
    delivery_status=models.CharField(default='Pending',max_length=255)
    payment_method=models.CharField(max_length=255,choices=PAYMENT)
    payment_status=models.BooleanField(default=False,null=True,blank=True)
    contact_no=models.CharField(max_length=15)
    address=models.CharField(max_length=100,null=True)
    created_at=models.DateTimeField(auto_now_add=True,null=True)
