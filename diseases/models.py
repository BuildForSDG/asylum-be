from django.db import models
from django.http import request

# Create your models here.

class Disease(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=200) #The disease name.
    description = models.TextField(blank=False, null=False)#Adescription about the disease.
    symptoms = models.TextField(blank=False, null=False) #Disease symptoms.
    source_url = models.URLField(blank=True, null=False) 
    writer = models.CharField(max_length=50) #The person/specialist who wrote about the disease.
    verified = models.BooleanField() #if the information is verified ir not.

    def __str__(self):
        return self.title
