from django.contrib.auth.models import User
from django.db import models
from model_utils.models import TimeStampedModel

__author__ = 'k1'


class Invoice(TimeStampedModel):
    paid_by = models.ForeignKey(User)