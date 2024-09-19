from django.contrib import admin
from apps.users.models import User

##PARA QUE SE VEAN LAS TABLAS EN EL DJANGO ADMIN
admin.site.register(User)

# Register your models here.
