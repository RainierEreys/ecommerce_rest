from apps.products.models import MeasureUnit, CategoryProduct, Product, Indicador
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from apps.products.api.serializers.product_serializer import ProductSerializer, ProductWriteSerializer

class ProductListAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        products = Product.objects.filter(state=True)
        return products
    
    
class ProductCreateAPIView(generics.CreateAPIView):
    serializer_class = ProductWriteSerializer
    # queryset = Product.objects.filer
    
    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'El producto se ha registrado exitosamente'})
        
        return Response(serializer.errors)
    
class ProductRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        return Product.objects.filter(state=True)
    
class ProductDestroyAPIView(generics.DestroyAPIView):
    serializer_class: ProductSerializer
    
    def get_queryset(self):
        return Product.objects.filter(state=True)
    
    def delete(self, request, pk=None):
        product = self.get_queryset().filter(id=pk).first()
        
        if product:
            product.state = False
            product.save()
            return Response({'message':'El producto se ha desactivado exitosamente'}, status=status.HTTP_200_OK)
        return Response({'error':'No existe un producto con estos datos'}, status=status.HTTP_404_NOT_FOUND)
    
class ProductUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ProductWriteSerializer
    
    def get_queryset(self):
        return Product.objects.filter(state=True)
    
    ##EXISTE UN METODO PATCH QUE SIRVE PARA TRAERNOS LA INSTANCIA EN CUESTION
    