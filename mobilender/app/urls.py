from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'client', views.ClientViewSet)
router.register(r'order', views.OrderViewSet)
router.register(r'product', views.ProductViewSet)
router.register(r'provider', views.ProviderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
