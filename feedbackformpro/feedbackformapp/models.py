from django.db import models


class FeedbackData(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField(max_length=100)
    rating = models.IntegerField()
    feedback = models.CharField(max_length=500)
