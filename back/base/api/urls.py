from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('licenses/', LicenseModelListCreateAPIView.as_view()),
    path('licenses/<int:pk>/', LicenseModelRetrieveUpdateDestroyAPIView.as_view()),
    path('licenses/<uuid:key>/activate/', LicenseActivateAPIView.as_view(), name='license_activate'),

    path('tickets/', TicketListCreateAPIView.as_view()),
    path('tickets/<int:pk>/', TicketRetrieveUpdateDestroyAPIView.as_view()),
    
    path('users/', UserListCreateAPIView.as_view()),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view()),

    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]