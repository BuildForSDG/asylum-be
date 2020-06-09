import json

from celery.utils.log import get_task_logger
from django.contrib.auth import get_user_model

from core.celery import app
from . models import Profile


logger = get_task_logger(__name__)
User = get_user_model()

@app.task(bind=True, retry_backoff=True, retry_backoff_max=20)
def create_user_profile(self, user_id, created):
    logger.info('Checking profile for user %s' % user_id)

    try:
        user = User.objects.get(pk=user_id)
        user_profile_qs = Profile.objects.filter(user=user)
        if created or not user_profile_qs:
            Profile.objects.create(user=user)
    except Exception as e:
        logger.error('ERROR: %s' % str(e))
        raise self.retry(exc=e, max_retries=3)


@app.task(bind=True, retry_backoff=True, retry_backoff_max=20)
def recommend_specialists(self, user_id):
    logger.info('Recommending specialists to user %s' % user_id)

    try:
        specialist_ids = []

        p = User.objects.get(pk=user_id)
        patient = Profile.objects.get(user=p)
        specialists = Profile.objects.filter(designation='specialist')
        for s in specialists:
            match = any(i in s.conditions.all() for i in patient.conditions.all())
            if match:
                specialist_ids.append(s.user.id)

        patient.recommended = json.dumps(specialist_ids)
        patient.save()
    except Exception as e:
        logger.error('ERROR: %s' % str(e))
        raise self.retry(exc=e, max_retries=3)
