from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views.fun_fact_view_set import FunFactViewSet
from api.views.popular_fun_facts_view_set import PopularFunFactViewSet

router = DefaultRouter()

router.register('dates', FunFactViewSet, basename='date')
router.register('popular', PopularFunFactViewSet, basename='popular')

app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
]
