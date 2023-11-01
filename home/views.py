from django.shortcuts import render,redirect
from products.models import *
# Create your views here.
def home(request):
    user = request.user
    cata = category.objects.all()
    if user.is_authenticated:
        len_cart = len(card.objects.filter(user=user))
        all_cart = card.objects.filter(user=user)
        total =0
        for i in all_cart:
            subtotal = i.product.new_price*i.quantity
            total+=subtotal
        
    return render(request, 'home/home.html',locals())

def shopping_cart(request):
    user = request.user
    if user.is_authenticated:
        all_cart = card.objects.filter(user=user)
        total =0
        for i in all_cart:
            subtotal = i.product.new_price*i.quantity
            total+=subtotal
    return render(request,'home/shopping-cart.html',locals())


def remove_cart(request,id):
    user = request.user
    prod = card.objects.filter(id=id, user=user)
    prod.delete()
    return redirect(request.META['HTTP_REFERER'])





def checkout(request):
    user = request.user
    if user.is_authenticated:
        all_cart = card.objects.filter(user=user)
        total =0
        for i in all_cart:
            subtotal = i.product.new_price*i.quantity
            total+=subtotal
    return render(request,'home/checkout.html',locals())