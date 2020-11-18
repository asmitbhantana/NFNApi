from rest_framework import generics, authentication, permissions
from django.contrib.auth import get_user_model
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from User.serializers import UserSerializer, AuthTokenSerializer

User = get_user_model()


class CreateUserView(generics.CreateAPIView):
    # create user using the serializers class
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    '''Create a new auth token for user'''
    serializer_class = AuthTokenSerializer
    '''Making the browser viewable token getting and setting platform'''
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES