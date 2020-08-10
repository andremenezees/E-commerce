
from django.urls import path

from ecommerce.base import views
from ecommerce.base.views import HomeView, ItemDetailView, add_to_cart, remove_from_cart, OrderSumarryView, checkout

app_name = 'base'
urlpatterns = [
    path('',  HomeView.as_view(), name='home'),
    path('checkout/', checkout, name='checkout'),
    path('order-summary/', OrderSumarryView.as_view(), name='order-summary'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove-to-cart/<slug>/', remove_from_cart, name='remove-from-cart'),


]
