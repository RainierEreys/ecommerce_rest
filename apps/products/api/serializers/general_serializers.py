from rest_framework import serializers
from apps.products.models import MeasureUnit, CategoryProduct, Indicador


class MeasureUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeasureUnit
        exclude = ('state', 'create_date', 'modification_date', 'deleted_date',)

class CategoryProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryProduct
        exclude = ('state', 'create_date', 'modification_date', 'deleted_date',)
        
class IndicadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indicador
        exclude = ('state', 'create_date', 'modification_date', 'deleted_date',)