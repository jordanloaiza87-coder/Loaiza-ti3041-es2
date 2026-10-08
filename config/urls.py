from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from catalogo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.lista_productos, name='inicio'),
    path('agregar-carrito/<int:producto_id>/', views.agregar_carrito, name='agregar_carrito'),
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    
    # Rutas para el administrador desde HTML
    path('registrar/', views.registrar_usuario, name='registrar_usuario'),
    path('agregar-producto/', views.agregar_producto, name='agregar_producto'),
    path('editar/<int:producto_id>/', views.editar_producto, name='editar_producto'),  # <-- ESTA ES LA QUE FALTA
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
    
    # Rutas de sesión
    path('login/', LoginView.as_view(template_name='catalogo/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='inicio'), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)