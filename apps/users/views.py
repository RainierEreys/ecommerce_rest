from django.contrib.sessions.models import Session
from rest_framework.views import APIView
from django.utils import timezone
from datetime import datetime
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token #modelo para obtener token para los usuarios que puedan acceder
from rest_framework.authtoken.views import ObtainAuthToken
from apps.users.api.serializers import UserTokenSerializer

#para hacer la fecha y hora consientes de la zona horaria
def get_aware_time():
    naive_datetime = datetime.now()
    aware_datetime = timezone.make_aware(naive_datetime)
    print(f'esta es ingenua {naive_datetime}')
    print(f'esta es consciente {aware_datetime}')
    return aware_datetime

class Login(ObtainAuthToken):
    
    def post(self, request, *args, **kwargs):
        login_serializer = self.serializer_class(data = request.data, context = {'request': request}) #ESTE SERIALIZADOR SOLO TIENE USERNAME Y PASSWORD
        if login_serializer.is_valid():
            user = login_serializer.validated_data['user']
            if user.is_active:
                user_serializer = UserTokenSerializer(user)
                #SI ESTA ACTIVO PUESSS... OBTENER TOKEN
                token, created = Token.objects.get_or_create(user = user)
                if created:
                    return Response({
                        'token': token.key,
                        'user': user_serializer.data,
                        'message': 'inicio de sesion exitoso'
                        }, status=status.HTTP_201_CREATED)
                else:
                    #PARA BORRAR TODAS LAS SESIONES QUE ESTEN ACTIVAS EN OTROS LADOS
                    all_session = Session.objects.filter(expire_date__gte = get_aware_time())
                    if all_session.exists():
                        for session in all_session:
                            session_data = session.get_decoded()
                            if user.id == int(session_data.get('_auth_user_id')):
                                session.delete()
                    #POR SI QUIERE INICIAR SESION EN OTRO NAVEGADOR
                    token.delete()
                    #Y SE LE GENERA UN NUEVO TOKEN
                    token = Token.objects.create(user=user)
                    return Response({
                        'token': token.key,
                        'user': user_serializer.data,
                        'message': 'inicio de sesion exitoso'
                        }, status=status.HTTP_201_CREATED)
                print('este usuario esta activo')
            else:
                return Response({"mensaje": "Este usuario no puede iniciar sesion"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({"mensaje":"Credenciales incorrectas"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"mensaje":"Hola, entraste"}, status=status.HTTP_200_OK)
        
class LogOut(APIView):
    
    def get(self, request, *args, **kwargs):
        try:
            token = request.GET.get('token') #HAY QUE ENVIARLE EL TOKEN COMO PARAMETRO EN LA PETICION (LA URL)
            ##LA MANERA DEL PROSPECT ES RECOGIENDO EL TOKEN DE EL ENCABEZADO "AUTHENTICATION"
            token = Token.objects.filter(key=token).first()
            print(token)
            if token:
                user = token.user 
                all_session = Session.objects.filter(expire_date__gte = get_aware_time())
                if all_session.exists():
                    for session in all_session:
                        session_data = session.get_decoded()
                        if user.id == int(session_data.get('_auth_user_id')):
                            session.delete()
                token.delete()
                session_message = 'Sesion de usuario eliminadas'
                token_message = 'Token eliminado'

                return Response({'token_message': token_message, 'session_message': session_message}, status= status.HTTP_200_OK)
            return Response({'message':'Error, no se ha encontrado usuario con esas credenciales'}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'message': 'No se ha completado el LogOut'}, status= status.HTTP_409_CONFLICT)    