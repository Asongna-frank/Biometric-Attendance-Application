from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from api.serializers.users import UserSerializer, LoginSerializer
from users.models import User
from api.permissions import UserPermissions

class UsersListViewset(viewsets.ModelViewSet):
    http_method_names = ['get', 'patch']
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_object(self):
        public_id = self.kwargs.get('pk')
        user = User.objects.get_object_by_public_id(public_id)
        return user

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "this is a private view"}, status=status.HTTP_200_OK)

class PublicView(APIView):
    def get(self, request):
        return Response({"message": "this is a public view"}, status=status.HTTP_200_OK)

class LoginView(viewsets.ViewSet):
    serializer_class = LoginSerializer
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
