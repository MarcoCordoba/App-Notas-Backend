from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = get_object_or_404(User, email=email)

    if not user.check_password(password):
        return Response({"error": "Invalid password"}, status=400)

    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)

    return Response({"token": token.key, "user": serializer.data})


@api_view(['POST'])
@permission_classes([AllowAny]) 
def register(request):
    nombre = request.data.get('nombre')
    apellido = request.data.get('apellido')
    correo = request.data.get('correo')
    password = request.data.get('password')

    if not all([nombre, apellido, correo, password]):
        return Response({'error': 'Faltan datos obligatorios.'}, status=400)

    username = f"{nombre}{apellido}".replace(" ", "").lower()

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Ya existe un usuario con ese nombre.'}, status=400)

    user = User.objects.create_user(
        username=username,
        email=correo,
        first_name=nombre,
        last_name=apellido,
        password=password
    )

    token = Token.objects.create(user=user)

    return Response({
        'token': token.key,
        'user': {
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name
        }
    })


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def profile(request):
    return Response({})
