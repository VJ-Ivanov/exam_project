from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):

    OPERATIONS = 'Operations'
    SALES = 'Sales'
    PRICING = 'Pricing'

    DEPARTMENTS = (
        (OPERATIONS, 'Operations'),
        (SALES, 'Sales'),
        (PRICING, 'Pricing'),
    )

    department = models.CharField(max_length=20, choices=DEPARTMENTS, default=OPERATIONS, blank=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

