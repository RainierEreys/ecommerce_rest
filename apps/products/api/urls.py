from django.urls import path
from apps.products.api.views.general_views import MeasureUnitListAPIView, IndicadorListAPIView, CategoryProductListAPIView
from apps.products.api.views.product_views import (ProductListAPIView, 
                                                   ProductCreateAPIView, 
                                                   ProductRetrieveAPIView,
                                                   ProductDestroyAPIView,
                                                   ProductUpdateAPIView)


urlpatterns = [
    path('measure_unit/', MeasureUnitListAPIView.as_view(), name = 'measure_unit'),
    path('indicador_list/', IndicadorListAPIView.as_view(), name = 'indicador'),
    path('category_product_list/', CategoryProductListAPIView.as_view(), name = 'category_product'),
    path('product/list/', ProductListAPIView.as_view(), name = 'productos'),
    path('product/create/', ProductCreateAPIView.as_view(), name = 'create_product'),
    path('product/retrieve/<int:pk>/', ProductRetrieveAPIView.as_view(), name = 'retrieve_product'),
    path('product/delete/<int:pk>/', ProductDestroyAPIView.as_view(), name = 'destroy_product'),
    path('product/update/<int:pk>/', ProductUpdateAPIView.as_view(), name = 'update_product')
]