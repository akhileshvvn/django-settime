from django.db import models
from django.contrib.auth.models import User

# Create your models here.

def mailid():
    return User.email

class formsyat(models.Model):
    Day = models.DateField()
    From = models.CharField(max_length=10)
    To = models.CharField(max_length=10)


