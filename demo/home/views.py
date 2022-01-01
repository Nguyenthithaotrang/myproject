from django.shortcuts import render
from .models import danhmucsanpham as danhmucsanpham_models
# Create your views here.

def get_home(request):
    danhmucsanpham_list = danhmucsanpham_models.objects.filter().order_by('danhmucsanpham_id')

    return render(request, 'index.html', {'danhmucsanpham_list' : danhmucsanpham_list})
