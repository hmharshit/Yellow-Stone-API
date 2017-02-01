from django.db import models
from django.core.validators import RegexValidator
# Create your models here.

class Passenger(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    phone_regex = RegexValidator(regex=r'^\+?9?1?([7-9]|1)?\d{9}$', message="Invalid phone number")
    phone_number = models.CharField(validators=[phone_regex], blank=True, max_length=15)
    gender = models.CharField(max_length=6)
    def __str__(self):
        return self.first_name + self.last_name
