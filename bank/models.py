from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    account_number = models.CharField(max_length=18, unique=True)
    options = (("savings", "savings"),
               ("current", "current"),
               ("credit", "credit"))
    account_type = models.CharField(max_length=16, choices=options, default="savings")
    balance = models.FloatField()
    phone_number = models.CharField(max_length=16)


class Transactions(models.Model):
    from_account_number = models.CharField(max_length=16)
    to_account_number = models.CharField(max_length=16)
    Amount = models.FloatField()
    Note = models.CharField(max_length=100)
    Date = models.DateField(auto_now=True)
