from django.db import models

# Create your models here.


class categ(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)

class products(models.Model):
    name=models.CharField(max_length=250,unique=True )
    slug=models.SlugField(max_length=250,unique=True)
    desc=models.TextField()
    img=models.ImageField()
    price=models.IntegerField()
    stock=models.IntegerField()
    available=models.BooleanField()
    category=models.ForeignKey(categ,on_delete=models.CASCADE)