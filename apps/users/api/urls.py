from django.urls import path
from apps.users.api.views import user_api_view, user_detail_view

urlpatterns = [
    path('usuario/', user_api_view, name="usuario_api"),
    path('usuario/<int:pk>/', user_detail_view, name='detalle_usuario')
]
