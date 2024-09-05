"""
URL configuration for proyecto2024B project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import (
    LoginView,
    LogoutView
)
from users.views import (
    first_view,
    second_view,
    base_view,
    list_view,
)
from products.views import products_list_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', first_view, name="first-view"),
    path('users2/', second_view, name="second-view"),
    path('list/', products_list_view, name="list-view"),
    path('', LoginView.as_view(template_name="base.html"), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
]
