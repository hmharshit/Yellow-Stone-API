from django.db import models
from django.core.validators import RegexValidator
# Create your models here.

class User(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(max_length=50,unique=True)
    phone_regex = RegexValidator(regex=r'^\+?9?1?([7-9]|1)?\d{9}$', message="Invalid phone number")
    phone_number = models.CharField(validators=[phone_regex], blank=True, max_length=15)

    class Meta:
        db_table = 'users'