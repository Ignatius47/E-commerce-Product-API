from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import CustomTokenObtainPairView, UserRegistrationView, UserDetailView

urlpatterns = [
    # JWT Token endpoints
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # User Registration
    path('register/', UserRegistrationView.as_view(), name='register'),

    # User Detail
    path('user/', UserDetailView.as_view(), name='user_detail'),
]