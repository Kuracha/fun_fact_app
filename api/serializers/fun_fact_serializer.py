from typing import Dict

from django.db import transaction
from rest_framework import serializers
import calendar
from fun_facts.models import FunFact


class FunFactSerializer(serializers.ModelSerializer):

    class Meta:
        model = FunFact
        fields = '__all__'

    def create(self, validated_data: Dict) -> FunFact:
        return self.update_or_create(validated_data)

    @transaction.atomic()
    def update_or_create(self, validated_data: Dict) -> FunFact:
        month = validated_data.get('month')
        day = validated_data.get('day')
        try:
            fun_fact = FunFact.objects.get(month=month, day=day)
        except FunFact.DoesNotExist:
            fun_fact = FunFact.objects.create(**validated_data)
        return fun_fact

    def to_representation(self, obj: FunFact) -> Dict:
        data = super().to_representation(obj)
        try:
            month = data['month']
            data['month'] = calendar.month_name[month]
        except (AttributeError, IndexError):
            pass
        return data
