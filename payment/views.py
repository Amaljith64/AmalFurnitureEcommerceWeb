from django.shortcuts import render, redirect, get_object_or_404
from shop.models import *
from cart.models import *
from cart.views import c_id
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.

def checkout(request,tot=0,count=0,ct_items=None):
    try:
        ct=cartlist.objects.get(cart_id=c_id(request))
        ct_items=items.objects.filter(cart=ct,active=True)
        for i in ct_items:
            tot +=(i.prodt.price*i.quan)
            count +=i.quan
    except ObjectDoesNotExist:
        pass
    return render(request,'checkout.html',{'t':tot})
