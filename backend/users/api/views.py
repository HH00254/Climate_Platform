from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

from users.api.serializers import (
    UserSerializer,
    UserRegistrationSerializer,
    UserLoginSerializer
)


class UserRegistrationView(APIView):
    """
    Summary:
    - API view for user registration.
    """

    def post(self, request):
        """
        Summary:
        - Handle POST request for user registration.
        """

        serializer = UserRegistrationSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            return Response(
                UserSerializer(user).data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
        
class UserLoginView(APIView):
    """_summary_

    Args:
        APIView (_type_): _description_
    """
    
    def post(self, request):
        """_summary_

        Args:
            request (_type_): _description_
        """
    
        serializer = UserLoginSerializer(data=request.data)
        
        serializer.is_valid(
            raise_exception=True
        )
        
        user = serializer.validated_data["user"]
        
        refresh = RefreshToken.for_user(user)
        
        return Response(
            {
                "refresh": str(refresh),
                "access":  str(refresh.access_token),
                "status":  str(status.HTTP_200_OK)
            }
        )
        
class CurrentUserView(APIView):
    """
        Summary:
        - Returns the currently authenticated user.
    """
    
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        """
            Summary:
                - Return information about the
                currently authenticated user.
        """
        
        serializer = UserSerializer(request.user)
        
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
        
        
