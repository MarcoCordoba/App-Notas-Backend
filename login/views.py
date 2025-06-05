from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = get_object_or_404(User, username=username)

    if not user.check_password(password):
        return Response({"error": "Invalid password"}, status=400)

    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)

    return Response({"token": token.key, "user": serializer.data})


@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.save()
        user.set_password(serializer.validated_data['password'])
        user.save()

        token = Token.objects.create(user=user)
        return Response({'token': token.key, 'user': serializer.data})

    return Response(serializer.errors, status=400)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def profile(request):

    


    return Response({})
