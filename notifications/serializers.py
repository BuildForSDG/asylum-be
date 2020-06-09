from rest_framework import serializers

from . models import Invitation, Message


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        exclude = ['mail_sent', ]


class InvitationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Invitation
        exclude = ['sender', 'accepted', 'mail_sent']
