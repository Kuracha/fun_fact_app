# Standard Library
from typing import Dict
from typing import List

# Django
from django.db import transaction

# Project
from api.providers.number_facts import NumberFactProvider
from api.serializers.base.month_name_serializer import BaseMonthNameSerializer
from fun_facts.models import FunFact


class FunFactSerializer(BaseMonthNameSerializer):
    class Meta(BaseMonthNameSerializer.Meta):
        fields = '__all__'
        read_only_fields = ['fact']

    def create(self, validated_data: Dict) -> FunFact:
        return self.update_or_create(validated_data)

    @transaction.atomic()
    def update_or_create(self, validated_data: Dict) -> FunFact:
        month = validated_data.get('month')
        day = validated_data.get('day')
        fact = NumberFactProvider().get_fact(month, day)
        try:
            fun_fact = FunFact.objects.get(month=month, day=day)
            if fact and fun_fact.fact != fact:
                fun_fact.fact = fact
                fun_fact.save()
        except FunFact.DoesNotExist:
            fun_fact = FunFact.objects.create(**validated_data, fact=fact)
        return fun_fact

    def get_unique_together_validators(self) -> List:
        return []
