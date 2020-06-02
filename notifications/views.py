from rest_framework import mixins, permissions, viewsets

from . models import Message
from . serializers import MessageSerializer


class MessageViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        sender = serializer.validated_data.get('sender', None)
        if sender:
            message = serializer.save()
        else:
            message = serializer.save(sender=self.request.user.email)

        # call task here
