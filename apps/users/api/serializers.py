from rest_framework import serializers
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    
    def create(self, validated_data):
        user = User(**validated_data)  
        ##set_password --> SIRVE PARA ENCRIPTAR CONTRASEÑA
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def update(self, instance, validated_data):
        updated_user = super().update(instance, validated_data)
        ##set_password --> SIRVE PARA ENCRIPTAR CONTRASEÑA
        updated_user.set_password(validated_data['password'])
        updated_user.save()
        return updated_user
    
        
class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  
    
    
    ##FUNC USADA PARA ESPECIFICAR QUE CAMPOS QUIERO RETURNAR EN EL JSON
    ##DE ESTA MANERA NO TENGO QUE LIMITAR "fields" EN EL SERIALIZER Y ME SIRVE PARA LISTAR, CREAR Y EDITAR AL MISMO TIEMPO
    ##TAMBIEN AYUDA A CAMBIAR ETIQUETAS EN EL LISTADO DE LOS DATOS (ver la de 'correo')
    def to_representation(self, instance):
        return {
            'id': instance['id'],
            'username': instance['username'],
            'correo-electronico': instance['email'],
            'clave': instance['password'],
        }
        
#EL SERIALIZER NO NECESARIAMENTE DEPENDE DE UN MODELO
# class TestUserSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length = 200)
#     email = serializers.EmailField()
    
#     #SECUENCIA DE VALIDACIONES DEL SERIALIZER
#     def validate_name(self, value):
#         if 'modafoka' in value:
            
#             raise serializers.ValidationError('Error, no puede existir un usuario con nombre repetido')
#         return value
    
#     def validate_email(self, value):
#         if value == '':
#             raise serializers.ValidationError('Tiene que indicar un correo')
#         return value
#         # print(self.context)
#         ##PARA HACERLO TODO DE UNA VEZ
#         # if self.validate_name(self.context['name']) in value:
#         #     raise serializers.ValidationError('el nombre no peude estar en el email')
#         # return value
    
#     def validate(self, data):
#         # if data['name'] in data['email']:
#         #     raise serializers.ValidationError('Error, el nombre no puede estar contenido enm el correo')
#         print(f'estoy en validate {data}')
#         return data
    
#     ##ESTE METODO ES LLAMADO CUANDO SE HACE .save()
#     #validated_data son los valores ya validados (ya pasaron las validaciones anteriores)
#     def create(self, validated_data):
#         print(f'metodo create a {validated_data}')
#         ##el asterisco es para pasar argumentos con clave, para que la clase sepa a que campo asignar cada valor
#         return User.objects.create(**validated_data)
    
#     ##ESTE METODO SE USA CUANDO SE ACTUALIZA Y ESOS SON LOS PARAMETROS QUE RECIBE
#     def update(self, instance, validated_data):
#         print(f'esta es la instancia {instance}')
#         instance.name = validated_data.get('name', instance.name)
#         instance.email = validated_data.get('email', instance.email)
#         instance.save()
#         return instance
    
#     ##SE PUEDE UTILIZAR CUANDO NO QUEREMOS QUE LO QUE LLENE EL USUARIO SEA ALMACENADO, SINO CUANDO 
#     ##POR EJEMPLO QUEREMOS QUE CUANDO LLLENE EL FORM ESA INFO SEA ENVIADA A MI CORREO
#     # def save(self):
#     #     print(self.validated_data)
#     #     send_email()
        
#     ##EXISTE .save() DEL SERIALIZADOR (create, update, save) Y DEL MODELO