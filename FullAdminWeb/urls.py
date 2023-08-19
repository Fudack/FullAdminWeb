from django.urls import path
from inventario.views import import_data ,export_data, product_list, contabilidad, recursosHumanos, facturacion
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from inicio.views import CustomLoginView, register, index

app_name = 'inventario'  # Esto establece el espacio de nombres

urlpatterns = [
    path('', CustomLoginView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('login/', CustomLoginView.as_view(), name='login'),  # Asegúrate de usar la barra '/' después de 'login'
    path('logout/', LogoutView.as_view(), name='logout'),  # Asegúrate de usar la barra '/' después de 'logout'
    path('index/', index, name='index'),
    path('register/', register, name='register'),
    path('inventario/', product_list, name='product_list'),  # Cambio de nombre para la vista principal
    path('export_data/', export_data, name='export_data'),
    path('import_data/', import_data, name='import_data'),
    path('contabilidad/', contabilidad, name='contabilidad'),
    path('recursosHumanos/', recursosHumanos, name='recursosHumanos'),
    path('facturacion/', facturacion, name='facturacion')
]
