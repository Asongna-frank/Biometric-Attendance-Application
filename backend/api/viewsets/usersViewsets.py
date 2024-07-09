from rest_framework import viewsets, status
from api.serializers.users import UserSerializer
from users.models import User


class UsersListViewset(viewsets.ModelViewSet):
    http_method_names = ['get', 'patch']

    serializer_class = UserSerializer

    queryset = User.objects.all()