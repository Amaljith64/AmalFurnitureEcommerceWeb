from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.


class categ(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)

    def __str__(self):
        return '{}'.format(self.name)     #to show name insted of object1,object2.....

class products(models.Model):
    name=models.CharField(max_length=250,unique=True )
    slug=models.SlugField(max_length=250,unique=True)
    desc=models.TextField()
    img=models.ImageField()
    price=models.IntegerField()
    stock=models.IntegerField()
    available=models.BooleanField()
    category=models.ForeignKey(categ,on_delete=models.CASCADE)


    def __str__(self):
        return '{}'.format(self.name)