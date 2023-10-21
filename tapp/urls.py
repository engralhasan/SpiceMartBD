from django.urls import path
from .views import index,remove_cart

urlpatterns = [
    path('', index,name='index'),
    path('remove_cart<int:id>', remove_cart,name='remove_cart'),
]