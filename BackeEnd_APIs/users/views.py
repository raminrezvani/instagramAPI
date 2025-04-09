from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer

User = get_user_model()

class SignUpView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'user': serializer.data,
                'token': str(refresh.access_token),
                'refresh': str(refresh),
                'message': 'User created successfully'
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SignInView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        print(f"Login attempt - Username: {username}")
        
        try:
            # Get the user object directly
            user = User.objects.get(username=username)
            print(f"User found: {user.username}")
            print(f"Password from request: {password}")
            
            # Try authentication
            authenticated_user = authenticate(request, username=username, password=password)
            print(f"Authentication result: {authenticated_user}")
            
            if authenticated_user is not None:
                refresh = RefreshToken.for_user(authenticated_user)
                return Response({
                    'token': str(refresh.access_token),
                    'refresh': str(refresh),
                    'user': {
                        'id': authenticated_user.id,
                        'username': authenticated_user.username,
                        'email': authenticated_user.email
                    }
                }, status=status.HTTP_200_OK)
            else:
                print("Authentication failed despite user existing")
                
        except User.DoesNotExist:
            print(f"User {username} not found in database")
            return Response({
                'error': 'User does not exist'
            }, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            print(f"Unexpected error: {str(e)}")
            return Response({
                'error': 'An error occurred during authentication'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response({
            'error': 'Invalid credentials'
        }, status=status.HTTP_401_UNAUTHORIZED)

class UserListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

class PublicUserListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
