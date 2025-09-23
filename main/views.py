from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.urls import reverse
from .models import *
from .forms import *
import datetime

# Create your views here.
# productList = [Product(name = "Bola 1", price = 100, description = "Bola pertama dijual", thumbnail = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/Football_Pallo_valmiina-cropped.jpg/250px-Football_Pallo_valmiina-cropped.jpg", category = "Bola futsal", is_featured = True, lingkar = 60, stock = 100), 
#                 Product(name = "Bola 2", price = 150, description = "Bola kedua dijual", thumbnail = "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/Basketball.png/250px-Basketball.png", category = "Bola basket", is_featured = True, lingkar = 70, stock = 10)
#                 ]

# Home Page View
@login_required(login_url="/login")
def homepage(request):
    filter_type = request.GET.get("filter", "all")

    if filter_type == "all":
        productList = Product.objects.all()
    else:
        productList = Product.objects.filter(user=request.user)
    
    return render(request, "HomePage.html", {"productList": productList, "username": request.user.username})

# Item Creation Form
@login_required(login_url="/login")
def createProduct(request):
    if request.method == "POST":
        creationForm = ProductCreationForm(request.POST)

        if (creationForm.is_valid()):
            # Attribute wajib
            user = request.user
            name = creationForm.cleaned_data["name"]
            price = creationForm.cleaned_data["price"]
            desc = creationForm.cleaned_data["description"]
            thumbnail = creationForm.cleaned_data["thumbnail"]
            category = creationForm.cleaned_data["category"]
            is_featured = creationForm.cleaned_data["is_featured"]

            # Attribute custom
            lingkar = creationForm.cleaned_data["lingkar"]
            stock = creationForm.cleaned_data["stock"]

            newBola = Product(user = user, name = name, price = price, description = desc, category = category, thumbnail = thumbnail, is_featured = is_featured, lingkar = lingkar, stock = stock)
            newBola.save()

            # Kembali ke Home Page
            return render(request, "HomePage.html", {"productList": Product.objects.all(), "username": request.user.username})
    else:
        creationForm = ProductCreationForm()
    return render(request, "ProductCreationPage.html", {"creationForm": creationForm})

# Product Details Page
@login_required(login_url="/login")
def productDetails(request, productId):
    product = get_object_or_404(Product, pk = productId)

    if not product:
        return render(request, "404.html", status=404)
    else:
        return render(request, "ProductDetailsPage.html", {"productViewed": product})

@login_required(login_url="/login")
def show_xml(request):
    productList = Product.objects.all()
    xml_data = serializers.serialize("xml", productList)
    return HttpResponse(xml_data, content_type="application/xml")

@login_required(login_url="/login")
def show_json(request):
    productList = Product.objects.all()
    json_data = serializers.serialize("json", productList)
    return HttpResponse(json_data, content_type="application/json")

@login_required(login_url="/login")
def show_xml_by_id(request, productId):
   try:
       product = Product.objects.filter(pk=productId)
       xml_data = serializers.serialize("xml", product)
       return HttpResponse(xml_data, content_type="application/xml")
   except Product.DoesNotExist:
       return HttpResponse(status=404)

@login_required(login_url="/login")
def show_json_by_id(request, productId):
    try:
       product = Product.objects.get(pk=productId)
       json_data = serializers.serialize("json", [product])
       return HttpResponse(json_data, content_type="application/json")
    except Product.DoesNotExist:
       return HttpResponse(status=404)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been successfully created!")
            return redirect("login")
    return render(request, "Register.html", {'form':form})

def login_user(request):
   if request.method == "POST":
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("homepage"))
        response.set_cookie("last_login", str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   return render(request, "Login.html", {'form':form})

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse("login"))
    response.delete_cookie("last_login")
    return response

# CHALLENGE 1.2
def addEmployee(request):
    newEmployee = Employee(name = "name", age = 10, pesona = "menawan")
    newEmployee.save()
    return render(request, "ViewEmployee.html", {"employee": newEmployee})

# CHALLENGE 2.3
def createCar(request):
    carList = Car.objects.all()

    if request.method == "POST":
        creationForm = CarCreationForm(request.POST)

        if (creationForm.is_valid()):
            # Attribute wajib
            name = creationForm.cleaned_data["name"]
            brand = creationForm.cleaned_data["brand"]
            stock = creationForm.cleaned_data["stock"]

            newCar = Car(name = name, brand = brand, stock = stock)
            newCar.save()

            # Kembali ke Home Page
            return render(request, "CarCreationPage.html", {"carList": carList, "creationForm": creationForm})
    else:
        creationForm = CarCreationForm()
    return render(request, "CarCreationPage.html", {"carList": carList, "creationForm": creationForm})