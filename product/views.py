import datetime
from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# Create your views here.


def product_create(request):
    context={
    "title":"Create"
    }
    return render(request,"product/index.html",context)

def product_detail(request):
    context={
    "title":"Create"
    }
    return render(request,"product/index.html",context)

def product_list(request):
    queryset=Product.objects.all()
    context={
        "title":"List"
    }
    today = datetime.datetime.now().date() 
    return render(request, "product/index.html", {'title':context,"object_list":queryset})  
    

def product_update(request):
    context={
    "title":"Create"
    }
    return render(request,"product/index.html",context)

def product_delete(request):
    context={
    "title":"Create"
    }
    return render(request,"product/index.html",context)

def hello(request):
    today = datetime.datetime.now().date()
    daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    return render(request, "product/hello.html", {"today" : today, "days_of_week" : daysOfWeek})


    


    
