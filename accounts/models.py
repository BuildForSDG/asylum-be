import json

from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models.signals import post_save
from django.utils import timezone

from disorders.models import Disorder


GENDER_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('unspecified', 'Unspecified')
)

DESIGNATIONS = (
    ('patient', 'Mental Health Patient'),
    ('specialist', 'Mental Health Specialist')
)

CURRENT_YEAR = timezone.now().year
ADULT_BIRTH_YEAR = CURRENT_YEAR - 18
CENTURY_AGO = CURRENT_YEAR - 100


class User(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]

    def __str__(self):
        return self.username if self.username else self.email

    @property
    def review_count(self):
        return self.reviewed.count()

    @property
    def average_rating(self):
        rating_list = self.reviewed.all().values_list('rating', flat=True)
        return sum(rating_list) / self.review_count


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(null=True, upload_to='avatars/%Y/%m/')
    gender = models.CharField(max_length=11, default='unspecified', choices=GENDER_CHOICES)
    designation = models.CharField(max_length=10, default='patient', choices=DESIGNATIONS)
    conditions = models.ManyToManyField(Disorder)
    managed_account = models.BooleanField(default=False)
    birth_year = models.PositiveIntegerField(
        default=ADULT_BIRTH_YEAR,
        validators=[MaxValueValidator(CURRENT_YEAR), MinValueValidator(CENTURY_AGO)]
    )

    recommended = models.CharField(max_length=50, default='')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.user.first_name:
            return 'Profile: %s' % self.user.get_full_name()
        return 'Profile: %s' % self.user.email

    @property
    def age(self):
        return CURRENT_YEAR - self.birth_year

    @property
    def is_patient(self):
        return True if self.designation == 'patient' else False

    @property
    def specialist_ids(self):
        if self.designation == 'patient' and self.recommended:
            return json.loads(self.recommended)
        return []


def on_user_saved(sender, instance, created, **kwargs):
    from . tasks import create_user_profile, recommend_specialists

    if instance.profile.is_patient:
        recommend_specialists.delay(instance.id)

    create_user_profile.delay(instance.id, created)


post_save.connect(on_user_saved, sender=User)
