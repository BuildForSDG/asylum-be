"""API URLs."""

from django.urls import path, include
from rest_framework import routers

from accounts.views import UserViewSet
from disorders.views import DisorderViewSet, SymptomViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('disorders', DisorderViewSet)
router.register('symptoms', SymptomViewSet)

urlpatterns = [

    path('auth/', include('rest_auth.urls')),

    path('auth/register/', include('rest_auth.registration.urls')),

]

urlpatterns += router.urls
