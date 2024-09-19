from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from apps.users.api.serializers import UserTokenSerializer


class Login(ObtainAuthToken):
    
    def post(self, request, *args, **kwargs):
        ##SERIALIZADOR YA DEFINIFDO (tiene un campo llamado user y otro llamado password)
        login_serializer = self.serializer_class(data = request.data, context = {'request':request})
        print(request.data)
        if login_serializer.is_valid():
            print('Paso validacion')
            user = login_serializer.validated_data['user']
            if user.is_active:
                print('Entraste')
                token,created = Token.objects.get_or_create(user=user)
                user_serializer = UserTokenSerializer(user)
                if created:
                    print(user_serializer.data)
                    return Response({
                        'token': token.key,
                        'user': user_serializer.data,
                        'message': 'Inicio de sesion exitoso'
                        }, status=status.HTTP_200_OK)
                else:
                    token.delete()
                    token = Token.objects.create(user=user)
                    return Response({'message': 'accesio con otro token',
                                    'token': token.key,
                                    'user': user_serializer.data,}, status=status.HTTP_201_CREATED)
            else:
                return Response({'message': 'Este usuario esta inhabilitado'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(login_serializer.errors, status=status.HTTP_400_BAD_REQUEST)