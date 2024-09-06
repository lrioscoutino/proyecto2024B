from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from products.models import Product

# Create your views here.
def products_list_view(request):
    products = Product.objects.all()
    context = {
        "products": products
    }
    return render(request, "product/list.html", context=context)

def product_create_view(request):
    if request.method == "POST":
        product = Product()
        product.name = request.POST['name']
        product.description = request.POST['description']
        product.price = request.POST['price']
        product.save()
        return redirect(reverse_lazy("list-products-view"))
    return render(request, "product/form.html" )

def product_update_view(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == "POST":
        product.name = request.POST['name']
        product.description = request.POST['description']
        product.price = request.POST['price']
        product.save()
        return redirect(reverse_lazy("list-products-view"))
    context = {
        "product": product
    }
    return render(
        request,
        "product/form.html",
        context=context
    )
