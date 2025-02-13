from django import forms 
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta :
        model = Product 
        fields = ["name", "desc", "price", "image","prod_type","offer_status", "offer_price","shipping_cost"]
        


