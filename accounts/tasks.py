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
