from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    phone_number = models.PositiveIntegerField(blank=False,null=False)
    dob = models.DateField(blank=False,null=False)

    

    