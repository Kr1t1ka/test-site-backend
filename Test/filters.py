from django_filters import rest_framework as filters

from .models import User


class UserFilter(filters.FilterSet):
    user_token = filters.CharFilter(field_name="jwt")
