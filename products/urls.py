from django.urls import path
from .views import products,add_to_cart,remove_cart

urlpatterns = [
    path('products/<int:id>/', products, name='products'),
    path('addtocart/<int:id>/', add_to_cart, name='addtocart'),
    path('remove_cart/<int:id>/', remove_cart, name='remove_cart'),
]