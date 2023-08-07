from django.conf import settings
from rest_framework import permissions


class DeleteWithAPIKeyPermission(permissions.BasePermission):
    def has_permission(self, request, view) -> bool:
        if request.method == 'DELETE':
            api_key = request.META.get('HTTP_X_API_KEY')
            return api_key == settings.SECRET_KEY
        return True
