from rest_framework import mixins, permissions, viewsets

from . models import Invitation, Message
from . serializers import InvitationSerializer, MessageSerializer
from . tasks import send_invitation, send_message


class MessageViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        sender = serializer.validated_data.get('sender', None)
        if sender:
            message = serializer.save()
        else:
            if self.request.user.is_authenticated:
                message = serializer.save(sender=self.request.user.email)

        send_message.delay(message.id)


class InvitationViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Invitation.objects.all()
    serializer_class = InvitationSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        i = serializer.save(sender=self.request.user)

        send_invitation.delay(i.id)
