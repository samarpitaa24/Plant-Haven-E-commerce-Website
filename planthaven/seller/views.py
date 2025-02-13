from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from .models import Product
from .forms import ProductForm
# Create your views here.


def add_prod(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")
        data = Product.objects.all()
    else:
        form = ProductForm()
        data = Product.objects.all()
    return render(request, 'seller/add_product.html', {'data':data, 'form' : form})


# def add_prod(request):
#     if request.method == "POST":
#     data = Product.objects.all()
#     form = ProductForm()
#     return render(request, 'seller/add_product.html', {'data':data, 'form' : form})


def update_data(request,id):
    if request.method == "POST":
        pi = Product.objects.get(pk=id)
        fm = ProductForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect("/")
    else :
        pi= Product.objects.get(pk=id)
        fm =ProductForm(instance=pi)
    return render(request, 'seller/update.html', {'form':fm})
    
    
def delete_data(request,id):
    if request.method=="POST":
        pi = Product.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect("/") #redirects on homepage