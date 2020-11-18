from rest_framework import generics, authentication, permissions
from django.contrib.auth import get_user_model
from User.serializers import UserSerializer

User = get_user_model()


class CreateUserView(generics.CreateAPIView):
    # create user using the serializers class
    serializer_class = UserSerializer
