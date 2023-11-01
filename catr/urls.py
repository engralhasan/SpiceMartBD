from django.urls import path
from .views import dec_qtybutton,inc_qtybutton

urlpatterns = [
    path('inc_qtybutton/<int:id>/', inc_qtybutton, name='inc_qtybutton'),
    path('dec_qtybutton/<int:id>/', dec_qtybutton, name='dec_qtybutton'),
]