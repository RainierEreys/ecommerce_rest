from rest_framework.routers import DefaultRouter
from apps.products.api.views.product_views import ProductViewSet
from apps.products.api.views.general_views import MeasureUnitListAPIView

router = DefaultRouter()

router.register(r'products', ProductViewSet, basename='Productos')
router.register(r'measures', ProductViewSet, basename='Medidas')
router.register(r'category-products', ProductViewSet, basename='Categoria de productos')
router.register(r'indicator-products', ProductViewSet, basename='Indicadores')

urlpatterns = router.urls