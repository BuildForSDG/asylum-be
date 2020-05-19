"""User filter."""

from django.contrib.auth import get_user_model
from django_filters import rest_framework as filters

User = get_user_model()


class UserFilter(filters.FilterSet):

    class Meta:
        model = User
        fields = [
            'profile__gender'
            'profile__designation',
        ]
