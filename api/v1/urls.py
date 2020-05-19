"""API URLs."""

from django.urls import path, include
from rest_framework import routers

from accounts.views import UserViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [

    path('auth/', include('rest_auth.urls')),

    path('auth/register/', include('rest_auth.registration.urls')),

]

urlpatterns += router.urls
