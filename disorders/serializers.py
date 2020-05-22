from rest_framework import serializers

from . models import Disorder, Symptom


class SymptomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Symptom
        exclude = ['created', ]


class DisorderSerializer(serializers.ModelSerializer):
    symptoms = SymptomSerializer(many=True)

    class Meta:
        model = Disorder
        exclude = ['created', 'slug']
