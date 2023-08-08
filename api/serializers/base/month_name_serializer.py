# Standard Library
import calendar
from typing import Dict

# 3rd-party
from rest_framework import serializers

# Project
from fun_facts.models import FunFact


class BaseMonthNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = FunFact
        fields = ['month']

    def to_representation(self, obj: FunFact) -> Dict:
        data = super().to_representation(obj)
        try:
            month = data['month']
            data['month'] = calendar.month_name[month]
        except (AttributeError, IndexError):
            pass
        return data
