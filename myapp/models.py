from collections.abc import Iterable
from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from django.utils.text import slugify
from account.models import Vendor

# Create your models here.

class MainCategory(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Category(models.Model):
    main_category = models.ForeignKey("MainCategory", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, default='slug')
    def __str__(self):
        return self.main_category.name + " > " + self.name
    
    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        super(Category,self).save(*args,**kwargs)


class SubCategory(models.Model):
    category = models.ForeignKey("Category", related_name='subcategory', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, default='slug')
    def __str__(self):
        return self.category.main_category.name + " > " + self.category.name + " > " + self.name
    
    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        super(SubCategory,self).save(*args,**kwargs)


class Item(models.Model):
    DRAFT = 'draft'
    WAITING_APPROVAL = 'waitingapproval'
    ACTIVE = 'active'
    STATUS = (
        (DRAFT,'Draft'),
        (WAITING_APPROVAL, 'Waiting approval'),
        (ACTIVE, 'Active')
    )
    status = models.CharField(max_length=50,choices=STATUS,default=DRAFT)
    image = models.ImageField(upload_to='images', default='images/image.png')
    name = models.CharField(max_length=100, unique=True)
    slug= models.SlugField(max_length=100)
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True)
    sub_category = models.ForeignKey("SubCategory",on_delete=models.SET_NULL, null=True)
    manufacturing_brand = models.CharField(max_length=50)
    model_name = models.CharField(max_length=100)
    color = models.CharField(max_length=15)
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    discount = models.IntegerField(default=0)
    price = models.IntegerField(validators=[MinValueValidator(1.00)])
    discounted_price = models.DecimalField(max_digits=8, decimal_places=2, default='self.price')
    description = models.TextField(max_length=1000)
    vendor = models.ForeignKey(Vendor,related_name='item', default='pk=1', on_delete=models.CASCADE)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    tags = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
    def avg_rating(self):
        reviews_total = 0
        for review in self.reviews.all():
            reviews_total += review.rating
        if reviews_total > 0:
            return reviews_total / self.reviews.count()
        return 0
    
    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        self.discounted_price = self.price - (self.discount/100 * self.price)
        super(Item,self).save(*args,**kwargs)


class AdminOffers(models.Model):
    admin_offer = models.CharField(max_length=100)
    def __str__(self):
        return self.admin_offer
    

class Banner(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images', default='images/image.png')
    def __str__(self):
        return self.name




