# from django.shortcuts import render
# from .models import CustomUser
# from rest_framework.generics import ListCreateAPIView
# from .serializers import CreateUserSerializer

# # Create your views here.
# class CustomerCreateView(ListCreateAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = CreateUserSerializer

from django.shortcuts import render
from .models import CustomUser
from rest_framework.generics import CreateAPIView
from .serializers import CreateUserSerializer
from rest_framework.response import Response
from rest_framework import status

class CustomerCreateView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CreateUserSerializer

    def create(self, request, *args, **kwargs):
        # Create the user without saving to the database
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # Set the user's password
        password = request.data.get('password')
        user.set_password(password)
        user.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
