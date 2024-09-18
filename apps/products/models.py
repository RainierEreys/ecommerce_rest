from django.db import models
from simple_history.models import HistoricalRecords
from apps.base.models import BaseModels
# Create your models here.

class MeasureUnit(BaseModels):
    
    description = models.CharField('Descripcion', max_length=200, unique=True, blank=False, null=False)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
        
    class Meta: 
        
        verbose_name = 'Unidad de Medida'
        verbose_name_plural = 'Unidades de Medida'
        
    def __str__(self):
        return self.description
    
    
class CategoryProduct(BaseModels):
    
    description = models.CharField('Descripcion', blank=False, null=False, unique=True, max_length=200)
    measure_unit = models.ForeignKey(MeasureUnit, on_delete=models.CASCADE, verbose_name='Unidad de Medida')
    historical = HistoricalRecords()
    
    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
    
    class Meta: 
        
        verbose_name = 'Categoría de Producto'
        verbose_name_plural = 'Categorías de Productos'
        
    def __str__(self):
        return self.description
    
class Indicador(BaseModels):
    
    descount_value = models.PositiveSmallIntegerField(default=0)
    category_product = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, verbose_name='Indicador de Oferta')
    historical = HistoricalRecords()
    
    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
    
    class Meta:
        db_table = 'Indicador de descuento por categoria'
        verbose_name = 'Indicador de Oferta'
        verbose_name_plural = 'Indicadores de Ofertas'
        
    def __str__(self):
        return (f'Oferta de la categoria {self.category_product}: {self.descount_value}')
    
class Product(BaseModels):
    
    name = models.CharField('Nombre del Producto', max_length=150, unique=True, blank=False, null=False)
    description = models.TextField('Descripcion de producto', blank=False, null=False)
    img = models.ImageField('Imagen del producto', upload_to='products/', blank=True, null=True)
    historical = HistoricalRecords()
    
    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        db_table = 'Productos'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        
    def __str__(self):
        return self.name

