from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def products(request,id):
    cat = category.objects.get(id = id)
    prod = product_all.objects.filter(category=cat)
    return render(request,'products/product.html',locals())


def add_to_cart(request, id):
    prod = product_all.objects.get(id=id)
    user = request.user
    if user.is_authenticated:
        try:
            pro = card.objects.filter(product=prod)
            if pro:
                for i in pro:
                    i.quantity += 1
                    i.save()
                    return redirect(request.META['HTTP_REFERER'])
            else:
                crt = card.objects.create(
                    user=user,
                    product=prod
                )
                crt.save()
                return redirect(request.META['HTTP_REFERER'])
        except Exception as e:
            print(e)
# def add_to_cart(request,id):
#     prod= product_all.objects.get(id=id)
#     user =request.user
#     if user.is_authenticated:
#         pro=card.objects.filter(product=prod,user=user)
#         if pro:
#             for i in pro:
#                 i.quantity+=1
#                 i.save()
#                 return redirect(request.META['HTTP_REFERER'])
#         else:
#             crt =card.objects.create(user=user,product=prod)
#         crt.save()
#         return redirect(request.META['HTTP_REFERER'])
            

def remove_cart(request,id):
    user = request.user
    prod = card.objects.filter(id=id, user=user)
    prod.delete()
    return redirect(request.META['HTTP_REFERER'])