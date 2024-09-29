from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import CustomTokenObtainPairView, UserRegistrationView, UserDetailView
from .views import api_root
from .views import UserProfileView


urlpatterns = [
    # JWT Token endpoints
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # User Registration
    path('register/', UserRegistrationView.as_view(), name='user-register'),

    # User Detail
    path('user/', UserDetailView.as_view(), name='user_detail'),

    path('', api_root, name='api-root'),  # Root API endpoint

    path('profile/', UserProfileView.as_view(), name='user-profile'),  # User profile URL

]