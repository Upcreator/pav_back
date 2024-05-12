from rest_framework import generics, permissions
from django.contrib.auth.models import User

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import *
from base.models import *

from rest_framework.response import Response
from rest_framework import status

from django.db.models import Count

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token
    
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LicenseModelListCreateAPIView(generics.ListCreateAPIView):
    queryset = LicenseModel.objects.all()
    serializer_class = LicenseModelSerializer
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, *args, **kwargs):
        user = request.user
        # Count the number of licenses associated with the user
        num_licenses = LicenseModel.objects.filter(user=user).count()
        if num_licenses < 3:
            # If the user has fewer than 3 licenses, allow creating a new license
            return super().post(request, *args, **kwargs)
        else:
            return Response({'message': 'You already have 3 licenses'}, status=status.HTTP_400_BAD_REQUEST)
        
class LicenseActivateAPIView(generics.UpdateAPIView):
    queryset = LicenseModel.objects.all()
    serializer_class = LicenseModelSerializer
    lookup_field = 'key'

    def update(self, request, *args, **kwargs):
        license_instance = self.get_object()
        if not license_instance:
            return Response({'error': 'License key not found'}, status=status.HTTP_404_NOT_FOUND)
        if license_instance.is_Activated:
            return Response({'error': 'License already activated'}, status=status.HTTP_400_BAD_REQUEST)
        license_instance.is_Activated = True
        license_instance.save()
        return Response({'message': 'License activated successfully'})

class LicenseModelRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LicenseModel.objects.all()
    serializer_class = LicenseModelSerializer