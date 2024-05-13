from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'productos', views.ProductoViewSet)
router.register(r'ventas', views.VentaViewSet)
router.register(r'detalleventas', views.DetalleVentaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
