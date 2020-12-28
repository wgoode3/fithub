from django.db import models
from user_app import User

class DailyStat(models.Model):
    day = models.DateField(auto_now_add=True)
    weight = models.FloatField()
    calories = models.FloatField()
    protein = models.FloatField()
    carbohydrates = models.FloatField()
    fats = models.FloatField()
    user = models.ForeignKeyField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
