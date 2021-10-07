from django.shortcuts import render
from django.views import View
from.models import *


class ProductView(View):
    def get(self, request):
        plants = Product.objects.filter(category='p')
        seeds = Product.objects.filter(category='s')
        bouquet = Product.objects.filter(category='b')
        fertilizer = Product.objects.filter(category='f')
        accessories = Product.objects.filter(category='a')
        return render(request, 'app/home.html', {'plants': plants, 'seeds': seeds, 'bouquet': bouquet, 'fertilizer': fertilizer, 'accessories': accessories})


class ProductDetailView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'app/productdetail.html', {'product': product})


def add_to_cart(request):
    return render(request, 'app/addtocart.html')


def buy_now(request):
    return render(request, 'app/buynow.html')


def profile(request):
    return render(request, 'app/profile.html')


def address(request):
    return render(request, 'app/address.html')


def orders(request):
    return render(request, 'app/orders.html')


def change_password(request):
    return render(request, 'app/changepassword.html')


def mobile(request):
    return render(request, 'app/mobile.html')


def login(request):
    return render(request, 'app/login.html')


def customerregistration(request):
    return render(request, 'app/customerregistration.html')


def checkout(request):
    return render(request, 'app/checkout.html')
