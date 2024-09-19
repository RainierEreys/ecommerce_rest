from django.contrib import admin
from apps.products.models import MeasureUnit, CategoryProduct, Indicador, Product

# Register your models here.
##PARA QUE EN EL DJANGO ADMIN SE VEA EL ID DEL OBJETO
class MeasureUnitAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')

##PARA QUE SE VEAN LAS TABLAS EN EL DJANGO ADMIN
admin.site.register(MeasureUnit, MeasureUnitAdmin)
admin.site.register(CategoryProduct)
admin.site.register(Indicador)
admin.site.register(Product)