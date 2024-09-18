from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from apps.users.models import User
from apps.users.api.serializers import UserSerializer, UserListSerializer
from rest_framework import status


@api_view(['GET', 'POST'])
#'request' porque es una funcion
def user_api_view(request):
    
    if request.method == 'GET':
        ##values() ---> PARA ESPECIFICAR LOS VALORES QUE SE QUIEREN LISTAR
        users = User.objects.all().values('id', 'username', 'email', 'password')
        #LISTADO
        users_serializer = UserListSerializer(users, many = True)
        
        # test_data = {
        #     'name': 'manimani',
        #     'email': 'test@gmail.com',
        # }
        
        # test_user = TestUserSerializer(data = test_data, context = test_data)
        # #SE LE ENVIA EL CONTEXTO PARA VALIDACIONES DE UN CAMPO QUE DEPENDAN DE OTRO QUE NO SE QUIERAN HACER EN EL VALIDATE SOLO
        # "is_valid SIEMPRE DEVUELVE TRUE O FALSE (SI ES FALSE DEVUELVE LOS ERRORES O MENSAJE ESPECIFICADO EN EL SERIALIZER)"
        # if test_user.is_valid():
        #     user_instance = test_user.save()
        #     print(user_instance)
        #     print('se pasaron las validaciones')
        # else:
        #     print(test_user.errors)
            
        
        # print(TestUserSerializer())
        
        #NO SE PUEDE ENVIAR LA VARIABLE DE MANERA DIRECTA (ESTA CONTENIDA EN UN ATRIBUTO LLAMADO 'data')
        return Response(users_serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        user_serializer = UserSerializer(data = request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors)
    
@api_view(['GET', 'PUT', 'DELETE'])
def user_detail_view(request, pk=None):
    #queryset
    user = User.objects.filter(id=pk).first()
    
    if user:
        
        if request.method == 'GET':
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'PUT':
            # 'request.data' AHI SIEMPRE SE ALMACENA LA INFO EN POST O PUT
            # CUANDO SE LE PASA LA INSTANCIA CON LA DATA EL FRAMEWORK ENTIENDE QUE DEBE ACTUALIZAR
            user_serializer = UserSerializer(instance = user, data = request.data) 
            print(user_serializer)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data, status=status.HTTP_200_OK)
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            user = User.objects.filter(id=pk).first()
            user.delete()
            return Response({'message': 'Usuario Eliminado Correctamente'}, status=status.HTTP_200_OK)
        
    return Response({'message': 'No se ha eliminado el usuario'}, status=status.HTTP_404_NOT_FOUND)