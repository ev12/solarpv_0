from django.shortcuts import render
import django_filters.rest_framework
from rest_framework import generics, viewsets, filters
from ..models import Product, Certificate, Service
from .serializers import ProductSerializer, CertificateSerializer, ServiceSerializer

class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['productName','=cellTechnology','cellManufacturer','=numCells']

class CertificateViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['=certID','reportNum','issueDate']

class ServiceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['=serviceID','description','=isFiRequired','=fiFrequency']
