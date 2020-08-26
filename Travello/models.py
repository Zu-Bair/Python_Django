from django.db import models

# Create your models here.


class Destination(models.Model):
    cityName = models.CharField(max_length=100)
    cityDesc = models.TextField()
    price = models.IntegerField()
    img = models.ImageField(upload_to='pics')
    offer =  models.BooleanField(default=False)