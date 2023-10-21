from django.shortcuts import render,redirect
from .models import addbtn

# Create your views here.
def index(r):
    if r.method =='POST':
        name=r.POST.get('name')
        add=addbtn.objects.create(name=name)
        add.save()
        return redirect('index')
    pro= addbtn.objects.all()
    
    
    return render(r,'index.html',locals())

def remove_cart(request,id):
    prod = addbtn.objects.filter(id=id)
    prod.delete()
    return redirect('index')