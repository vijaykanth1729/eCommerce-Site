from django.urls import path
from .views import view, update_to_cart

app_name = 'carts'
urlpatterns = [
    path('view/', view, name='view'),
    path('cart/<slug:slug>/', update_to_cart, name='update_to_cart'),

 ]
