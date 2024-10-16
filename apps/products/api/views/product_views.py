from apps.products.models import MeasureUnit, CategoryProduct, Product, Indicador
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework import generics
from apps.users.authentication_mixins import Authentication
from apps.products.api.serializers.product_serializer import ProductSerializer, ProductWriteSerializer

class ProductViewSet(Authentication, viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = ProductSerializer.Meta.model.objects.filter(state=True)
    
    def list(self, request):
        print(self.user) #MUESTRA EL USER GRACIAS A QUE HEREDA 'AUTHENTICATION'
        product_serializer = self.get_serializer(self.queryset, many=True)
        return Response(product_serializer.data, status=status.HTTP_200_OK)

class ProductListAPIView(generics.ListAPIView):
    
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        
        products = Product.objects.filter(state=True)
        return products
    
    
class ProductCreateAPIView(Authentication, generics.ListCreateAPIView):
    serializer_class = ProductWriteSerializer
    # queryset = Product.objects.filer
    queryset = ProductSerializer.Meta.model.objects.filter(state = True)    
    
    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'El producto se ha registrado exitosamente'})
        
        return Response(serializer.errors)
    
class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id = pk, state = True).first()
    
    def put(self, request, pk=None):
        if self.get_queryset(pk):
            product_serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            
            if product_serializer.is_valid():
                product_serializer.save()
                return Response(product_serializer.data, status=status.HTTP_200_OK)
            return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)       
    
    def delete(self, request, pk=None):
        product = self.get_queryset().filter(id=pk).first()
        
        if product:
            product.state = False
            product.save()
            return Response({'message':'El producto se ha desactivado exitosamente'}, status=status.HTTP_200_OK)
        return Response({'error':'No existe un producto con estos datos'}, status=status.HTTP_404_NOT_FOUND)
    
    
# class ProductDestroyAPIView(generics.DestroyAPIView):
#     serializer_class: ProductSerializer
    
#     def get_queryset(self):
#         return Product.objects.filter(state=True)
    
#     def delete(self, request, pk=None):
#         product = self.get_queryset().filter(id=pk).first()
        
#         if product:
#             product.state = False
#             product.save()
#             return Response({'message':'El producto se ha desactivado exitosamente'}, status=status.HTTP_200_OK)
#         return Response({'error':'No existe un producto con estos datos'}, status=status.HTTP_404_NOT_FOUND)
    
class ProductUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ProductWriteSerializer
    
    def get_queryset(self):
        return Product.objects.filter(state=True)
    
    ##EXISTE UN METODO PATCH QUE SIRVE PARA TRAERNOS LA INSTANCIA EN CUESTION
    