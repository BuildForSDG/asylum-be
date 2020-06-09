from rest_framework import filters, permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from api.permissions import IsSpecialistOrReadOnly
from . models import Disorder, Symptom
from . serializers import DisorderSerializer, SymptomSerializer


class DisorderViewSet(viewsets.ModelViewSet):
    queryset = Disorder.objects.filter(verified=True).select_related().prefetch_related()
    serializer_class = DisorderSerializer
    permission_classes = [permissions.IsAuthenticated, IsSpecialistOrReadOnly]

    @action(detail=True, methods=['get'])
    def add_symptom(self, request, pk=None):
        disorder = self.get_object()
        title = request.GET.get('title', None)

        if title:
            try:
                symptom, _ = Symptom.objects.get_or_create(title=title)
                disorder.symptoms.add(symptom)
                serializer = SymptomSerializer(symptom)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Exception as e:
                resp = {'message': str(e)}
                return Response(resp, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        resp = {'message': 'A symptom title is required'}
        return Response(resp, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get'])
    def remove_symptom(self, request, pk=None):
        disorder = self.get_object()
        symptom_id = request.GET.get('symptom_id', None)

        if symptom_id:
            try:
                disorder.symptoms.remove(int(symptom_id))
                return Response({'message': 'OK'}, status=status.HTTP_200_OK)
            except Exception as e:
                resp = {'message': str(e)}
                return Response(resp, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        resp = {'message': 'A valid symptom id is required'}
        return Response(resp, status=status.HTTP_400_BAD_REQUEST)


class SymptomViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Symptom.objects.all()
    serializer_class = SymptomSerializer
    filter_backends = [filters.SearchFilter, ]
    search_fields = ['title', ]
