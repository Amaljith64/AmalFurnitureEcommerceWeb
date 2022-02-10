from django.shortcuts import render
from . models import *

# Create your views here.

def home(request,):
 return render(request,'index.html')

def shop(request):
 prod=products.objects.all()

 return render(request,'shop.html',{'pr':prod})



def detail(request):
 return render(request,'productdetails.html')