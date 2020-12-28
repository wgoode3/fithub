from django.db import models
from django.contrib.auth.models import User

User._meta.get_field('email')._unique = True
User._meta.get_field('email').blank = False
User._meta.get_field('email').null = False

class Profile(models.Model):
    GENDER = (
        ("MALE", "MALE"),
        ("FEMALE", "FEMALE"),
        ("OTHER", "OTHER")
    )

    user = models.OneToOneField(User, on_delete=models.Cascade)
    goal_weight = models.FloatField()
    height = models.FloatField()
    gender = models.CharField(choices=GENDERS)
    date_of_birth = models.DateField()
    updated_at = models.DateTimeField(auto_now=True)
