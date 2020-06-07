from rest_framework import serializers

from . models import Review


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        exclude = ['created', ]
        extra_kwargs = {
            'target': {'write_only': True},
            'reviewer': {'read_only': True}
        }
