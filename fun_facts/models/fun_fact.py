# Django
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models


class FunFact(models.Model):
    month = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)], default=1)
    day = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(31)], default=1)
    fact = models.TextField()

    class Meta:
        verbose_name = 'Fun Fact'
        constraints = [
            models.UniqueConstraint(fields=['month', 'day'], name="%(class)s_month_day_uniq_constraint")
        ]

    def __str__(self):
        return f'{self.month}/{self.day}'
