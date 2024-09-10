from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('crear_tema/', views.crear_tema, name='crear_tema'),
    path('crear_articulo/', views.crear_articulo, name='crear_articulo'),
    # path('articulos_por_tema/<int:tema_id>/', views.articulos_por_tema, name='articulos_por_tema'),

]
