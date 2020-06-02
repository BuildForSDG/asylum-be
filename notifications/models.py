from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Message(models.Model):
    sender = models.EmailField(null=True)
    name = models.CharField(max_length=99, blank=True)
    recipient = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    subject = models.CharField(max_length=99, blank=True)
    body = models.TextField()

    mail_sent = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Message: %s' % self.timestamp

    def save(self, *args, **kwargs):
        if not self.subject:
            self.subject = 'Message From %s' %(self.name if self.name else self.sender)
        super(Message, self).save(*args, **kwargs)
