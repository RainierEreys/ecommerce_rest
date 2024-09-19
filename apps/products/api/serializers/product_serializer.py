from rest_framework import serializers
from apps.products.models import Product
from apps.products.api.serializers.general_serializers import MeasureUnitSerializer, CategoryProductSerializer


class ProductSerializer(serializers.ModelSerializer):
    measure_unit = serializers.StringRelatedField() ##VA A TOMAR LO QUE SE HAYA DEFINIDO EN EL METODO __str__ DEL MODELO(SI SE INSTANCIA LA CLASE DEL SERIALIZADOR ME MUESTRA TODOS LOS CAMPOS DEL MODELO)
    category_product = serializers.StringRelatedField()
    
    class Meta:
        model = Product
        exclude = ('state', 'create_date', 'modification_date', 'deleted_date',)
        
class ProductWriteSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Product
        fields = '__all__'
        