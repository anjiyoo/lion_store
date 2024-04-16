from django.urls import path
from . import views

app_name = 'customer'

urlpatterns = [
    path("", views.customer_index, name='index'),
    path("food_detail/<int:pk>", views.food_detail, name='food_detail'),
    path("add_cart/", views.add_cart, name='add_cart'),
    path("remove_cart/", views.remove_cart, name='remove_cart'),
    path("modify_cart/", views.modify_cart, name='modify_cart'),
]