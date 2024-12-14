from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from apps.users.application.serializers.user_serializer import UserSerializer
from apps.users.application.commands.register_user_command import RegisterUserCommand
from apps.users.domain.services.user_service import UserService
from apps.users.infrastructure.repositories_impl import DjangoUserRepository

class RegisterUserView(APIView):
    @swagger_auto_schema(
        operation_description="Register a new user",
        request_body=UserSerializer,
        responses={
            status.HTTP_201_CREATED: UserSerializer,
            status.HTTP_400_BAD_REQUEST: openapi.Response('Bad Request', UserSerializer),
        },
    )
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user_repo = DjangoUserRepository()
            user_service = UserService(user_repo)
            command = RegisterUserCommand(user_service)
            try:
                user_aggregate = command.execute(
                    username=serializer.validated_data['username'],
                    email_str=serializer.validated_data['email'],
                    password=request.data.get('password')  # Handle password securely
                )
                response_data = {
                    "id": user_aggregate.user.id,
                    "username": user_aggregate.user.username,
                    "email": user_aggregate.user.email.address,
                    "roles": [role.name for role in user_aggregate.roles],
                    "profile": user_aggregate.profile
                }
                return Response(response_data, status=status.HTTP_201_CREATED)
            except ValueError as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
