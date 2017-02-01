from django.db import models

# Create your models here.

class Passenger(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    phone_number = models.CharField(max_length=15)
    # Integer field will not preserve leading 0, +, and spacing.
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    def __str__(self):
        return self.first_name + self.last_name
