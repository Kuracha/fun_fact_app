# 3rd-party
from rest_framework import serializers

# Project
from api.serializers.base.month_name_serializer import BaseMonthNameSerializer
from fun_facts.models import FunFact


class PopularFunFactsSerializer(BaseMonthNameSerializer):
    days_checked = serializers.SerializerMethodField()

    class Meta(BaseMonthNameSerializer.Meta):
        fields = ('id', 'month', 'days_checked')

    def get_days_checked(self, obj: FunFact) -> int:
        days = FunFact.objects.filter(month=obj.month).count()
        return days
