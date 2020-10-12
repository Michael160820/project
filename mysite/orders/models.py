
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from offers.models import Offer


class Order(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=255)
    body = models.TextField(max_length=1000)
    amount = models.IntegerField()
    published = models.DateTimeField(default=timezone.now)
    deadline_date = models.DateTimeField('deadline date')
    offers = models.ManyToManyField(Offer)
    email = models.EmailField(max_length=70, null=True, blank=True, unique=True)
    phone_number = models.IntegerField(max_length=13, default=0)

