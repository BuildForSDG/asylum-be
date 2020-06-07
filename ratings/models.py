from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

User = get_user_model()


class Review(models.Model):
    reviewer = models.ForeignKey(User, related_name='review', on_delete=models.CASCADE)
    target = models.ForeignKey(User, related_name='reviewed', on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(10)])
    review = models.TextField(null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Review: %s' % self.pk
