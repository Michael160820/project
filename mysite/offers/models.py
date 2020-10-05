from django.db import models

class Offer(models.Model):
    price = models.IntegerField
    comment = models.CharField(max_length=250)
