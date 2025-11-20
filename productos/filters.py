import django_filters
from .models import Producto

class ProductoFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name="precio", lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name="precio", lookup_expr='lte')
    nombre = django_filters.CharFilter(field_name="nombre", lookup_expr='icontains')

    class Meta:
        model = Producto
        fields = ['min_price', 'max_price', 'nombre']   