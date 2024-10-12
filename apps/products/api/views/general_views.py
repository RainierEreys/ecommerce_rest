from apps.products.models import MeasureUnit, CategoryProduct, Indicador
from rest_framework import generics, viewsets
from apps.products.api.serializers.general_serializers import MeasureUnitSerializer, CategoryProductSerializer, IndicadorSerializer


##LISTAPIVIEW ES PARA DEVOLVER UN CONJUNTO DE VALORES (NO UNO SOLO)
class MeasureUnitListAPIView(viewsets.ModelViewSet):
    serializer_class = MeasureUnitSerializer
    
    # def get_queryset(self):
    #     measures = MeasureUnit.objects.filter(state=True) ##PARA QUE FILTRE LAS QUE ESTAN EN ESTADO ACTIVO
    #     return measures
    
class IndicadorListAPIView(viewsets.ModelViewSet):
    serializer_class = IndicadorSerializer
    
    # def get_queryset(self):
    #     indicador = Indicador.objects.filter(state=True) ##PARA QUE FILTRE LAS QUE ESTAN EN ESTADO ACTIVO
    #     return indicador
   
class CategoryProductListAPIView(viewsets.ModelViewSet):
    serializer_class = CategoryProductSerializer
    
    # def get_queryset(self):
    #     indicador = CategoryProduct.objects.filter(state=True) ##PARA QUE FILTRE LAS QUE ESTAN EN ESTADO ACTIVO
    #     return indicador 

    