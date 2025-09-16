from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core import serializers
from .models import *
from .forms import *

# Create your views here.
productList = [Product(name = "Bola 1", price = 100, description = "Bola pertama dijual", thumbnail = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/Football_Pallo_valmiina-cropped.jpg/250px-Football_Pallo_valmiina-cropped.jpg", category = "Bola futsal", is_featured = True, lingkar = 60, stock = 100), 
                Product(name = "Bola 2", price = 150, description = "Bola kedua dijual", thumbnail = "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/Basketball.png/250px-Basketball.png", category = "Bola basket", is_featured = True, lingkar = 70, stock = 10)
                ]

# Home Page View
def homepage(request):
    productList = Product.objects.all
    return render(request, "HomePage.html", {"productList": productList})

# Item Creation Form
def createProduct(request):
    if request.method == "POST":
        creationForm = ProductCreationForm(request.POST)

        if (creationForm.is_valid()):
            # Attribute wajib
            name = creationForm.cleaned_data["name"]
            price = creationForm.cleaned_data["price"]
            desc = creationForm.cleaned_data["description"]
            thumbnail = creationForm.cleaned_data["thumbnail"]
            category = creationForm.cleaned_data["category"]
            is_featured = creationForm.cleaned_data["is_featured"]

            # Attribute custom
            lingkar = creationForm.cleaned_data["lingkar"]
            stock = creationForm.cleaned_data["stock"]

            newBola = Product(name = name, price = price, description = desc, category = category, thumbnail = thumbnail, is_featured = is_featured, lingkar = lingkar, stock = stock)
            newBola.save()

            # Kembali ke Home Page
            return homepage(request=request)
    else:
        creationForm = ProductCreationForm()
    return render(request, "ProductCreationPage.html", {"creationForm": creationForm})

# Product Details Page
def productDetails(request, productId):
    product = get_object_or_404(Product, pk = productId)

    if not product:
        return render(request, "404.html", status=404)
    else:
        return render(request, "ProductDetailsPage.html", {"productViewed": product})

def show_xml(request):
    productList = Product.objects.all()
    xml_data = serializers.serialize("xml", productList)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    productList = Product.objects.all()
    json_data = serializers.serialize("json", productList)
    return HttpResponse(json_data, content_type="application/json")

def show_xml_by_id(request, productId):
   try:
       product = Product.objects.filter(pk=productId)
       xml_data = serializers.serialize("xml", product)
       return HttpResponse(xml_data, content_type="application/xml")
   except Product.DoesNotExist:
       return HttpResponse(status=404)

def show_json_by_id(request, productId):
    try:
       product = Product.objects.get(pk=productId)
       json_data = serializers.serialize("json", [product])
       return HttpResponse(json_data, content_type="application/json")
    except Product.DoesNotExist:
       return HttpResponse(status=404)


# CHALLENGE 2
def addEmployee(request):
    newEmployee = Employee(name = "name", age = 10, pesona = "menawan")
    newEmployee.save()
    return render(request, "ViewEmployee.html", {"employee": newEmployee})