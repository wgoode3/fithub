from django.db import models
from django.contrib.auth.models import User

User._meta.get_field('email')._unique = True
User._meta.get_field('email').blank = False
User._meta.get_field('email').null = False

class Profile(models.Model):
    GENDERS = (
        ("MALE", "Male"),
        ("FEMALE", "Female"),
        ("OTHER", "I prefer not to answer")
    )

    user = models.OneToOneField(User, related_name="my_profile", on_delete=models.CASCADE)
    # TODO user_avatar
    goal_weight = models.FloatField()
    height = models.FloatField()
    gender = models.CharField(max_length=6, choices=GENDERS)
    date_of_birth = models.DateField()
    updated_at = models.DateTimeField(auto_now=True)
