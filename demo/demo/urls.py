"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home import views as home
from sanpham import views as sanpham
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home.get_home),
    path('home/product.html/', sanpham.get_sanpham),
    path('home/about.html/', sanpham.get_about),
    path('home/contact.html/', sanpham.get_contact),
    path('home/services.html/', sanpham.get_services),
    path('home/single.html/', sanpham.get_contact),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT )

admin.site.site_header = "Mocoloco"