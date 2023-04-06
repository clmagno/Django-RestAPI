from django.db import models

# Create your models here.
class Event(models.Model):

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)