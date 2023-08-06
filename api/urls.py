from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views.fun_fact_view_set import FunFactViewSet

router = DefaultRouter()

router.register('dates', FunFactViewSet)

app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
]
