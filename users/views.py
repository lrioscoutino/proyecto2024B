from django.shortcuts import render
from django.http.response import HttpResponse


# Create your views here.
def first_view(request):
    return HttpResponse("<h1>Hola</h1>")

def second_view(request):
    name = "Luis Rios"
    age = 47
    age_list = [23,4,6,72,1,4]
    contexto = {
        "name": name,
        "age": age,
        "listas":age_list,
    }
    print(f">>>>> {request.method}")
    return render(
        request,
        "index.html",
        context=contexto
    )

def base_view(request):
    return render(
        request,
        "base.html"
    )

def list_view(request):
    return render(
        request,
        "list.html"
    )
