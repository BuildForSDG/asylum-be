"""User filter."""

from django.contrib.auth import get_user_model
from django_filters import rest_framework as filters

User = get_user_model()


class UserFilter(filters.FilterSet):
    category = filters.CharFilter(field_name='profile__designation', lookup_expr='iexact')
    gender = filters.CharFilter(field_name='profile__gender', lookup_expr='iexact')

    class Meta:
        model = User
        fields = {
            'username': ['icontains', ],
            'email': ['icontains', ],
            'first_name': ['icontains', ],
            'last_name': ['icontains', ],
        }
