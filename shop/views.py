from django.shortcuts import render, get_object_or_404
from .models import *


# Create your views here.

def home(request, ):
    return render(request, 'index.html')


def shop(request, c_slug=None):
    c_page = None
    prodt = None
    if c_slug != None:
        c_page = get_object_or_404(categ, slug=c_slug)
        prodt = products.objects.filter(category=c_page, available=True)
    else:
        prodt = products.objects.all().filter(available=True)
    cat = categ.objects.all()

    return render(request, 'shop.html', {'pr': prodt, 'ct': cat})


def detail(request):
    return render(request, 'productdetails.html')
