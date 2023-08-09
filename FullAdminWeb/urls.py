"""
URL configuration for FullAdminWeb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from inventario.views import  export_data, inventario, contabilidad, recursosHumanos, facturacion
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from inicio.views import CustomLoginView, register, index

urlpatterns = [
    path('', CustomLoginView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('login', CustomLoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('index/', index, name='index'),
    path('register/', register, name='register'),
    path('inventario/', inventario, name='inventario'),
    path('export_data/', export_data, name='export_data'),
    path('contabilidad/', contabilidad, name='contabilidad'),
    path('recursosHumanos/', recursosHumanos, name='recursosHumanos'),
    path('facturacion/', facturacion, name='facturacion')
]
