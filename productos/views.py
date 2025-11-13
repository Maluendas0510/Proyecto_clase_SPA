from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, filters ,generics
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from .models import Producto
from .serializers import ProductoSerializer, RegisterSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProductoFilter



class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    
    # Puedes agregar filtros, búsquedas y ordenamientos aquí si es necesario
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nombre', 'descripcion', 'precio', 'tipo' ]
    filterset_class = ProductoFilter
    
    ordering_fields = ['nombre', 'precio', 'tipo']
    ordering = ['nombre']  # Ordenamiento por defecto
    
    
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]  
