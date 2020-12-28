from django.db import models
from stat_app import DailyStat

UNITS = (
    # non-dimensional
    ("SERVING", "SERVING"),
    ("SLICE", "SLICE"),
    ("PACKAGE", "PACKAGE"),
    ("PACKET", "PACKET"),
    ("BOWL", "BOWL"),
    ("BAR", "BAR"),
    ("CUP", "CUP"),
    # volume
    ("TEASPOON", "TEASPOON"),
    ("TABLESPOON", "TABLESPOON"),
    ("FLUID OUNCE", "FLUID OUNCE"),
    ("CUP", "CUP"),
    ("PINT", "PINT"),
    ("MILLILITER", "MILLILITER"),
    ("LITER", "LITER"),
    # mass
    ("OUNCE", "OUNCE"),
    ("GRAM", "GRAM")
)

class Food(models.Model):
    name = models.CharField()
    calories_per_amount = models.FloatField()
    protein_per_amount = models.FloatField()
    carbohydrates_per_amount = models.FloatField()
    fats_per_amount = models.FloatField()
    serving_size = models.FloatField()
    units = models.CharField(choices=UNITS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class FoodAmount(models.Model):
    value = models.FloatField()
    units = models.CharField(choices=UNITS)
    food = models.ForeignKeyField(Food, on_delete=models.CASCADE)
    day = models.ForeignKeyField(DailyStat, related_name="meals", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
