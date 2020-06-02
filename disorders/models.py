from django.db import models
from django.utils.text import slugify


class Symptom(models.Model):
    title = models.CharField(max_length=99)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def disorder_count(self):
        return self.disorder_set.count()


class Disorder(models.Model):
    title = models.CharField(max_length=99)
    slug = models.SlugField(max_length=99, null=True, blank=True)
    description = models.TextField()
    symptoms = models.ManyToManyField(Symptom)
    external_link = models.URLField()
    verified = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Disorder, self).save(*args, **kwargs)

    @property
    def user_count(self):
        pass
