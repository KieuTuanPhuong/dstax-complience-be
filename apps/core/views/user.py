from rest_framework import viewsets

from ..filters import UserFilter
from ..models import User
from ..serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @property
    def filterset_class(self):
        return UserFilter
