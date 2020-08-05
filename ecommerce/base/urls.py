
from django.urls import path

from ecommerce.base import views

app_name = 'base'
urlpatterns = [
    path('',  views.item_list, name='item_list'),
    path('checkout/', views.checkout, name='checkout'),
    path('products/', views.products, name='products'),

]
