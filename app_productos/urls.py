from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_productos, name='listar_productos'),
    path('agregar/', views.agregar_producto, name='agregar_producto'),
    path('<int:pk>/', views.ver_producto, name='ver_producto'),
    path('editar/<int:pk>/', views.editar_producto, name='editar_producto'),
    path('eliminar/<int:pk>/', views.eliminar_producto, name='eliminar_producto'),
]