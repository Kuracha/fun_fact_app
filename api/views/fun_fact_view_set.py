from rest_framework.exceptions import MethodNotAllowed
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.serializers.fun_fact_serializer import FunFactSerializer
from fun_facts.models import FunFact


class FunFactViewSet(ModelViewSet):
    serializer_class = FunFactSerializer
    queryset = FunFact.objects.all()
    http_method_names = ['get', 'post', 'delete']

    def retrieve(self, request, *args, **kwargs) -> Response:
        raise MethodNotAllowed('GET')
