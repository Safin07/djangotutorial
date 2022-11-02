from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.say_hello), # Passing a reference to the function. Routes always end with a forward slash "/"
    path('', views.index),
    path('catalog', views.catalog),
    path('products/', views.get_all_products),
    path('products/', views.get_produts),

]
