from .models import *
from .views import *


def count(request):
    item_count = 0;
    if 'admin' in request.path:
        return {}
    else:
        try:
            ct = cartlist.objects.filter(cart_id=c_id(request))
            cti = items.objects.all().filter(cart=ct[:1])
            for c in cti:
                item_count += c.quan

        except cartlist.DoesNotExist:
            item_count = 0
        return dict(itc=item_count)


def checkout(request, tot=0, count=0, ct_items=None):
    try:
        ct = cartlist.objects.get(cart_id=c_id(request))
        ct_items = items.objects.filter(cart=ct, active=True)
        for i in ct_items:
            tot += (i.prodt.price * i.quan)
            count += i.quan
    except ObjectDoesNotExist:
        pass
    return dict(t=tot)
