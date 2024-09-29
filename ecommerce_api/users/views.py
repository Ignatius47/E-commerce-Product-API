from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import CustomUserSerializer
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from .serializers import UserProfileSerializer

User = get_user_model()  # Ensure this retrieves your CustomUser model

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Custom JWT serializer to include additional user data in the token response.
    """
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['is_staff'] = user.is_staff  # Include whether the user is staff in the token
        return token

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class UserRegistrationView(APIView):
    """
    API view to handle user registration. Creates a new user and returns a JWT token.
    """
    permission_classes = [AllowAny]  # Allow anyone to access this view

    def post(self, request, *args, **kwargs):
        # Use the CustomUserSerializer to validate incoming user data
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            # Generate token for the registered user
            token = CustomTokenObtainPairSerializer.get_token(user)
            refresh_token = str(token)
            access_token = str(token.access_token)

            return Response({
                "message": "User registered successfully",
                "access_token": access_token,
                "refresh_token": refresh_token,
                "user": {
                    "username": user.username,
                    "email": user.email,
                }
            }, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


@api_view(['GET'])
def api_root(request, format=None):
    """
    Root API endpoint that lists all available API endpoints in the e-commerce API.
    """
    return Response({
        'products': {
            'list': reverse('product-list', request=request, format=format),
            'create': reverse('product-list', request=request, format=format),
            'detail': reverse('product-detail', args=[1], request=request, format=format),
        },
        'users': {
            'register': reverse('user-register', request=request, format=format),
            'login': reverse('token_obtain_pair', request=request, format=format),  # Login URL
            'profile': reverse('user-profile', request=request, format=format),
        },
        'auth': {
            'token_refresh': reverse('token_refresh', request=request, format=format),  # Token refresh URL
        }
    })

class UserProfileView(generics.RetrieveAPIView):
    """
    API view to retrieve the currently logged-in user's profile.
    """
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        """
        Override get_object to return the profile of the authenticated user.
        """
        return self.request.user