from django.db import models
from stat_app.models import DailyStat

UNIT_CHOICES = (
    ('non-dimensional', (
            ('serving', 'serving'),
            ('slice', 'slice'),
            ('package', 'package'),
            ('packet', 'packet'),
            ('bowl', 'bowl'),
            ('cup', 'cup'),
            ('bar', 'bar')
        )
    ),
    ('volume', (
            ('teaspoon', 'teaspoon'),
            ('tablespoon', 'tablespoon'),
            ('fluid ounce', 'fluid ounce'),
            ('cup', 'cup'),
            ('pint', 'pint'),
            ('milliliter', 'milliliter'),
            ('liter', 'liter')
        )
    ),
    ('mass', (
            ("ounce", "ounce"),
            ("gram", "gram")
        )
    )
)

class Food(models.Model):
    name = models.CharField(max_length=255)
    calories_per_amount = models.FloatField()
    protein_per_amount = models.FloatField()
    carbohydrates_per_amount = models.FloatField()
    fats_per_amount = models.FloatField()
    serving_size = models.FloatField()
    units = models.CharField(max_length=11, choices=UNIT_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class FoodAmount(models.Model):
    value = models.FloatField()
    units = models.CharField(max_length=11, choices=UNIT_CHOICES)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    day = models.ForeignKey(DailyStat, related_name="meals", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
