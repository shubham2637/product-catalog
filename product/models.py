from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=256)
    quantity = models.IntegerField(default=1)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"{self.name} uploaded : {self.quantity}"