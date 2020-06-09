"""API URLs."""

from django.urls import path, include
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

from accounts.views import UserViewSet
from disorders.views import DisorderViewSet, SymptomViewSet
from notifications.views import InvitationViewSet, MessageViewSet
from ratings.views import ReviewViewSet

schema_view = get_swagger_view(title='Asylum API Docs')

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('disorders', DisorderViewSet)
router.register('symptoms', SymptomViewSet)
router.register('messages', MessageViewSet)
router.register('reviews', ReviewViewSet)
router.register('invitations', InvitationViewSet)

urlpatterns = [

    path('auth/', include('rest_auth.urls')),

    path('auth/register/', include('rest_auth.registration.urls')),

    path('docs/', schema_view)

]

urlpatterns += router.urls
