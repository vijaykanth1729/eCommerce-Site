from django.urls import path
from .views import home, single, search

app_name = 'products'

urlpatterns = [
    path('', home, name='home'),
    path('s/', search, name='search'),
    path('products/<slug:slug>/', single, name='detail'),
]
