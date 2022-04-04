from django.db import models


# Create your models here.


class Paisa(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    country= models.TextField()
    address=models.TextField()

    amount = models.CharField(max_length=100)
    payment_id = models.CharField(max_length=100)
    paid = models.BooleanField(default=False)
