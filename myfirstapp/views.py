from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def say_hello(request):
    data = {'name': 'Neo'}
    return render(request, 'hello.html', data)
  
def index(request):
    return render(request, 'index.html')
  
  
def catalog(request):
    return render(request, 'catalog.html')
  
from .models import Product

def get_all_products(request):
    products = Product.objects.all()
    html = ''
    for p in products:
        html += f'<h1>{p.id} - {p.title}<h1><span>{p.description}</span>'
    
    return HttpResponse(html)
  
def get_produts(request):
    data = {'products': Product.objects.all()}
    return render(request, 'products.html', data)

