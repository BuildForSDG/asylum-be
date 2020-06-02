"""API URLs."""

from django.urls import path, include
from rest_framework import routers

from disorders.views import DisorderViewSet, SymptomViewSet
from notifications.views import MessageViewSet

router = routers.DefaultRouter()
router.register('disorders', DisorderViewSet)
router.register('symptoms', SymptomViewSet)
router.register('messages', MessageViewSet)

urlpatterns = [

    path('auth/', include('rest_auth.urls')),

    path('auth/register/', include('rest_auth.registration.urls')),

]

urlpatterns += router.urls
