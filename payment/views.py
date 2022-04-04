from django.shortcuts import render, redirect, get_object_or_404
from shop.models import *
from cart.models import *
from cart.views import c_id
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

import razorpay

from .models import Paisa

from django.views.decorators.csrf import csrf_exempt


# def checkout(request, tot=0, count=0, ct_items=None):
#     try:
#         ct = cartlist.objects.get(cart_id=c_id(request))
#         ct_items = items.objects.filter(cart=ct, active=True)
#         for i in ct_items:
#             tot += (i.prodt.price * i.quan)
#             count += i.quan
#     except ObjectDoesNotExist:
#         pass
#     return render(request, 'base.html', {'t': tot})


def subash(request, tot=0, count=0, ct_items=None):

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        country = request.POST.get("country")
        address = request.POST.get("address")
        amount = int(request.POST.get("amount")) * 100
        client = razorpay.Client(auth=("rzp_test_ZY4ulZfKRFRCrI", "7ExtOPzLE2HVDB8cJdcTnFYV"))
        payment = client.order.create({'amount': amount, 'currency': 'INR', 'payment_capture': '1'})
        print(payment)
        pay = Paisa(name=name, amount=amount, payment_id=payment['id'],email=email,country=country,address=address)
        pay.save()
        return render(request, 'checkout.html', {'payment': payment})

    try:
     ct = cartlist.objects.get(cart_id=c_id(request))
     ct_items = items.objects.filter(cart=ct, active=True)
     for i in ct_items:
            tot += (i.prodt.price * i.quan)
            count += i.quan
    except ObjectDoesNotExist:
            pass

    return render(request, 'checkout.html',{'t':tot})


@csrf_exempt
def success(request):
    if request.method == "POST":
        a = request.POST
        order_id = ""
        for key, val in a.items():
            if key == 'razorpay_order_id':
                order_id = val
                break
        user = Paisa.objects.filter(payment_id=order_id).first()
        user.paid = True
        user.save()
    return render(request, 'success.html')
