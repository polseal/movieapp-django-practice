from rest_framework.permissions import BasePermission
from django.contrib.auth.models import AnonymousUser # to be able to open in swagger

class IsAuthenticatedForDelete(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        if request.method == 'DELETE':
            user_info = f"{request.user} {request.user.is_authenticated}"
            print(user_info)
            return request.user and request.user.is_authenticated
        return False
class AllowGetAuthenticatedForAll(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        # For other methods, check if the user is authenticated
        return request.user and request.user.is_authenticated