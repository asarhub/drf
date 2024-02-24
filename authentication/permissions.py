from rest_framework.permissions import BasePermission, IsAuthenticated
from authentication.models import User
class IsUserAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return isinstance(request.user, User)

class IsActiveUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_active == True

class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser == True