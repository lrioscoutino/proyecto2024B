from django.shortcuts import render
from products.models import Product

# Create your views here.
def products_list_view(request):
    products = Product.objects.all()
    context = {
        "products": products
    }
    return render(request, "list.html", context=context)
