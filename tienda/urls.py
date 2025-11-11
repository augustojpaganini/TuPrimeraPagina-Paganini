from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('camiseta/', views.camiseta_form, name='camiseta'),
    path('equipo/', views.equipo_form, name='equipo'),
    path('cliente/', views.cliente_form, name='cliente'),
    path('camisetas/', views.lista_camisetas, name='lista_camisetas'),
    path('equipos/', views.lista_equipos, name='lista_equipos'),
    path('equipos/<slug:slug>/', views.camisetas_por_equipo, name='camisetas_por_equipo'),
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('carrito/agregar/<int:camiseta_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/eliminar/<int:camiseta_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('buscar/', views.buscar_camisetas, name='buscar_camisetas'),

]
