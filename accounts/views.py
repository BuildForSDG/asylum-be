"""User views."""

from django.contrib.auth import get_user_model
from rest_framework import viewsets

from . filters import UserFilter
from . serializers import UserSerializer


User = get_user_model()


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all().select_related()
    filterset_class = UserFilter
