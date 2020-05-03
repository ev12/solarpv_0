from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'product', views.ProductViewSet)
router.register(r'services', views.ServiceViewSet)
router.register(r'certificates', views.CertificateViewSet)

app_name = 'backend'

urlpatterns = [
    path('', include(router.urls)),
]
