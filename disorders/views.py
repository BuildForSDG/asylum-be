from rest_framework import viewsets

from . models import Disorder
from . serializers import DisorderSerializer


class DisorderViewSet(viewsets.ModelViewSet):
    queryset = Disorder.objects.filter(verified=True).select_related().prefetch_related()
    serializer_class = DisorderSerializer
