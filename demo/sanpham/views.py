from django.shortcuts import render
from .models import sanpham as sanpham_models
# Create your views here.
def get_sanpham(request):
    return render(request, 'product.html')

def get_about(request):
    return render(request, 'about.html')

def get_contact(request):
    return render(request, 'contact.html')

def get_services(request):
    return render(request, 'services.html')

def get_single(request):
    return render(request, 'single.html')