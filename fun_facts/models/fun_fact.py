# Django
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models


class FunFact(models.Model):
    month = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)], default=1)
    day = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(31)], default=1)
    fact = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Fun Fact'
        unique_together = ('month', 'day')

    def __str__(self) -> str:
        return f'{self.month}/{self.day}'
