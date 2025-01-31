from django.urls import path
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.PantallaInicial),
    path('PantallaInicial/', views.PantallaInicial, name='Pantalla Principal'),
    path('PantallaReceta/', views.PantallaReceta, name='PantallaReceta'),
    path('PerfilUsuario/', views.PantallaUsuario, name='Pantalla Perfil Usua'),
    path('PantallaBusqueda/', views.PantallaBusqueda, name='PantallaBusqueda'),
    path('pantallaRegistroReceta/', views.pantallaRegistroReceta, name='pantallaRegistroReceta'),
    path('pantallaRegistroUsuario/', views.pantallaRegistroUsuario, name='pantallaRegistroUsuario'),
    path('pantallaRegistroIngrediente/', views.PantallaRegistroIngrediente, name='PantallaRegistroIngrediente')

]