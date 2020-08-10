
from django.urls import path

from ecommerce.base import views
from ecommerce.base.views import HomeView, ItemDetailView, add_to_cart, remove_from_cart

app_name = 'base'
urlpatterns = [
    path('',  HomeView.as_view(), name='home'),
    path('checkout/', views.checkout, name='checkout'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove-to-cart/<slug>/', remove_from_cart, name='remove-from-cart'),

]
