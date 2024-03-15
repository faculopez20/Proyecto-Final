from django.urls import path
from Producto import views

urlpatterns = [
    path('Raqueta/', views.Raqueta.as_view(), name='Raqueta'),
    path('Raqueta/nuevo/', views.CrearRaqueta.as_view(), name='crear_Raqueta'),
    path('Raqueta/nuevo/', views.CrearRaqueta.as_view(), name='crear_Raqueta'),
    path('Raqueta/<int:pk>/', views.DetalleRaqueta.as_view(), name='detalle_Raqueta'),
    path('Raqueta/<int:pk>/editar/', views.EditarRaqueta.as_view(), name='editar_Raqueta'),
    path('Raqueta/<int:pk>/eliminar/', views.EliminarRaqueta.as_view(), name='eliminar_Raqueta'),
]