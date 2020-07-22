from django.db import models

# Create your models here.


class contactdata(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.BigIntegerField()
    email = models.EmailField(max_length=100)
    course = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
