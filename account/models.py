from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db.models import Q

# Create your models here.

class UserProfile(models.Model):
    user=models.OneToOneField(User,related_name='userprofile',on_delete=models.CASCADE)
    is_vendor=models.BooleanField(default=False)
    def __str__(self):
        return self.user.username
    
class Vendor(models.Model):
    user=models.OneToOneField(User,related_name='vendor', on_delete=models.CASCADE)
    store_name = models.CharField(max_length=50, unique=True)
    gst_number = models.CharField(max_length=15,validators=[MinLengthValidator(15)])
    pickup_address1 = models.CharField(max_length=50)
    pickup_address2 = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=6, validators=[MinLengthValidator(6)])
    def __str__(self):
        return self.user.username


class Address(models.Model):
    user = models.ForeignKey(User,related_name='address',on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    zip_code = models.CharField(max_length=6, validators=[MinLengthValidator(6)])
    set_primary = models.BooleanField(default=False)
    def save(self, *args, **kwargs):
        if self.set_primary:
            self.__class__._default_manager.filter(user=self.user, set_primary=True).update(set_primary=False)
        super().save(*args, **kwargs)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user'],
                condition=Q(set_primary=True),
                name='unique_primary_per_user'
            )]
        ordering = ['-set_primary']
    def __str__(self):
        return self.user.username

