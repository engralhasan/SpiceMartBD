from django.urls import path
from .views import home,shopping_cart,remove_cart,checkout


urlpatterns = [
    path('',home,name='home'),
    path('shopping_cart',shopping_cart,name='shopping_cart'),
    path('remove_cart/<int:id>',remove_cart,name='remove_cart'),
    path('checkout',checkout,name='checkout'),
]
