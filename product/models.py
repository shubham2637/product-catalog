from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=256)
    quantity = models.IntegerField(default=1)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return f"{self.name} uploaded : {self.quantity}"

