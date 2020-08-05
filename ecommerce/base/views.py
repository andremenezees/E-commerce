from django.shortcuts import render


def item_list(request):
    return render(request, 'base/home.html')


def checkout(request):
    return render(request, 'base/checkout.html')


def products(request):
    return render(request, 'base/products.html')
