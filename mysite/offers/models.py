
from django.db import models
from django.utils import timezone

class Offer(models.Model):
    price = models.IntegerField
    comment = models.CharField(max_length=250)
    answered = models.DateTimeField(default=timezone.now)
    email = models.EmailField(max_length=70, null=True, blank=True, unique=True)
    phone_number = models.IntegerField(max_length=13, default=0)



