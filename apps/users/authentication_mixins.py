from apps.users.authentication import ExpiringTokenAuthentication
from rest_framework.authentication import get_authorization_header
from rest_framework.response import Response

class Authentication(object):
    
    def get_user(self, request):
        token = get_authorization_header(request).split()
        if token:
            try:
                token = token[1].decode()
                print(token)
            except:
                return None
        return None
    
    def dispatch(self, request, *args, **kwargs): #ES EL METODO QUE SE EJECUTA ANTES QUE TODO (VALIDO PARA HACER VALIDACIONES Y MODIFICACIONES ANTES QUE CORRA TODO)
        user = self.get_user(request)
        return super().dispatch(request, *args, **kwargs)
    