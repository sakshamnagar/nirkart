from django.db import models
from myapp.models import Item
from django.contrib.auth.models import User
from account.models import UserProfile
from django.core.validators import MinLengthValidator
# Create your models here.

class DeliveryCharges(models.Model):
    delivery = models.IntegerField()
    def __str__(self):
        return str(self.delivery)


class Order(models.Model):
    ORDER_PLACED = 'Order_Placed'
    ORDER_CONFIRMED = 'Order_Confirmed'
    ORDER_SHIPPED = 'Order_Shipped'
    ORDER_CANCELLED = 'Order_Cancelled'
    STATUS = (
        (ORDER_PLACED, 'Order Placed'),
        (ORDER_CONFIRMED, 'Order Confirmed'),
        (ORDER_SHIPPED, 'Order Shipped'),
        (ORDER_CANCELLED, 'Order Cancelled'),
    )
    status = models.CharField(max_length=50,choices=STATUS,default=ORDER_PLACED)
    order_id = models.AutoField(primary_key=True)
    review = models.BooleanField(default=False)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order')
    item_image = models.ImageField(default='images/image.png')
    item_id = models.CharField(max_length=15)
    item_name = models.CharField(max_length=100)
    item_price = models.IntegerField()
    item_discounted_price = models.FloatField()
    item_quantity = models.IntegerField(default=0)
    item_discount = models.IntegerField()
    item_vendor = models.CharField(max_length = 50)
    address1 = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=6, validators=[MinLengthValidator(6)])
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__ (self):
        return str(self.order_id)
    

class Reviews(models.Model):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    RATING = (
        (ONE, 1),
        (TWO, 2),
        (THREE, 3),
        (FOUR, 4),
        (FIVE, 5),
    )

    review = models.TextField(max_length = 500)
    rating = models.IntegerField(choices = RATING)
    item = models.ForeignKey(Item, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name='reviews', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return '(' + self.user.username + ')' + self.item.name