from django.shortcuts import render,redirect
from products.models import card

# Create your views here.
def dec_qtybutton(request,id):
    prod=card.objects.get(id=id,)
    prod.quantity+=1
    prod.save()
    return redirect(request.META['HTTP_REFERER'])

 


def inc_qtybutton(request,id):
    prod=card.objects.get(id=id,)
    if prod==0:
        prod.delete()
    else:
        prod.quantity-=1
        prod.save()
    return redirect(request.META['HTTP_REFERER'])