from rest_framework import status, viewsets
from rest_framework.response import Response

from . models import Review
from . serializers import ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all().select_related()

    def perform_create(self, serializer):
        target = serializer.validated_data.get('target', None)
        if not target.profile.is_patient:
            qs = Review.objects.filter(reviewer=self.request.user, target=target)
            if qs:
                review = self.serializer_class(qs.first(), self.request.data)
                if review.is_valid():
                    review.save()
                else:
                    return Response(review.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save(reviewer=self.request.user)
