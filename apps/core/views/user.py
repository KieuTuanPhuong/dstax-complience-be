from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from ..filters import UserFilter
from ..models import User
from ..serializers import UserSerializer


@extend_schema(tags=["Core: User"])
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @property
    def filterset_class(self):
        return UserFilter
