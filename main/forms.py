from django import forms
from django.core.exceptions import ValidationError
from django.utils.html import strip_tags
from .models import *

class ProductCreationForm(forms.Form):
    # Attribute wajib
    name = forms.CharField(max_length=255)
    price = forms.IntegerField()
    description = forms.CharField(max_length=255)
    thumbnail = forms.URLField()
    category = forms.CharField()
    is_featured = forms.BooleanField()
    
    # Attribute custom
    lingkar = forms.FloatField()
    stock = forms.IntegerField()

    def checkNameValid(self):
        name = self.cleaned_data["name"]
        takenNames = Product.objects.all()
        if (name not in takenNames) and (len(name) <= 100):
            return strip_tags(name)
        else:
            raise ValidationError("Invalid name!")
        
    def checkDescValid(self):
        desc = self.cleaned_data["description"]
        if (len(desc) <= 100):
            return strip_tags(desc)
        else:
            raise ValidationError("Description must be at most 100 words long!")
    
    def checkPriceValid(self):
        price = self.cleaned_data["price"]
        if (price > 0):
            return strip_tags(price)
        else:
            raise ValidationError("Price must be a postive integer!")
        
    def checkStockValid(self):
        stock = self.cleaned_data["stock"]
        if (stock > 0):
            return strip_tags(stock)
        else:
            raise ValidationError("Stock must be a postive integer!")
    
    def checkSizeValid(self):
        size = self.cleaned_data["size"]
        if (size > 0):
            return strip_tags(size)
        else:
            raise ValidationError("Stock must be a postive float!")
    
    def checkCategoryValid(self):
        category = self.cleaned_data["category"]
        return strip_tags(category)

# CHALLENGE 2.2
class CarCreationForm(forms.Form):
    name = forms.CharField(max_length=255)
    brand = forms.CharField(max_length=255)
    stock = forms.IntegerField()