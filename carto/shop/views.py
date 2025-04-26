from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def v_home(request):
    product_data = product.objects.all()


    catprods = Product_details.objects.values('category','id')
    
    allprods = []
    cats = {i['category'] for i in catprods}
    cat_titles = []
    for cat in cats:
        prods = Product_details.objects.filter(category=cat)
        prods_chunked = [prods[i:i+4] for i in range(0,len(prods),4)]
        allprods.append(prods_chunked)

        # Get title from first product if available
        if prods:
            cat_titles.append(prods[0].category)
        else:
            cat_titles.append("Products")



    return render(request, "comps/home.html", {'data_chunks': allprods,'cat_titles':cat_titles})

def v_about(request):
    return HttpResponse("This is the about page.")

def v_contact(request):
    return HttpResponse("This is the Contact page.")

def v_tracker(request):
    return HttpResponse("This is the product tracking page.")

def v_search(request):
    return HttpResponse("This is the search page.")

def v_productview(request):
    return HttpResponse("This is the product View page.")

def v_checkout(request):
    return HttpResponse("This is the checkout page.")