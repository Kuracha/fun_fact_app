from rest_framework import viewsets, status
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.response import Response

from api.serializers.popular_fun_fact_serializer import PopularFunFactsSerializer
from fun_facts.models import FunFact


class PopularFunFactViewSet(viewsets.ModelViewSet):
    serializer_class = PopularFunFactsSerializer
    queryset = FunFact.objects.all().distinct('month')
    http_method_names = ['get']

    def retrieve(self, request, *args, **kwargs) -> Response:
        raise MethodNotAllowed('GET')

    def list(self, request, *args, **kwargs) -> Response:
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        serialized_data = serializer.data
        sorted_data = sorted(serialized_data, key=lambda x: x['days_checked'], reverse=True)
        return Response(sorted_data, status=status.HTTP_200_OK)
