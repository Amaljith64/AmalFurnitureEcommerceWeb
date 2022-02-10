from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
# Create your models here.


class categ(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)

    def __str__(self):
        return '{}'.format(self.name)     #to show name insted of object1,object2.....

    def get_url(self):
        return reverse('prod_cat',args=[self.slug])   #to add link in category @shop

class products(models.Model):
    name=models.CharField(max_length=250,unique=True )
    slug=models.SlugField(max_length=250,unique=True)
    desc=models.TextField()
    img=models.ImageField()
    price=models.IntegerField()
    stock=models.IntegerField()
    available=models.BooleanField()
    category=models.ForeignKey(categ,on_delete=models.CASCADE)


    def get_url(self):
        return reverse('detail',args=[self.category.slug,self.slug])



    def __str__(self):
        return '{}'.format(self.name)