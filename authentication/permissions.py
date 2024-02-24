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

class Dummypermission(BasePermission):
    #Dummy permission helpfull for development purpose, because we cant develop the things keeping the restrictions
    message = "This is a dummy permission name given, where all the users can access the data"
    def has_permission(self, request, view):
        #True means details of users will come
        return True
        # False means message will come

class Dummypermission2(BasePermission):
    #Dummy permission helpfull for development purpose, because we cant develop the things keeping the restrictions
    message = "This is a dummy permission name given, where all the users can access the data"
    def has_permission(self, request, view):
        #True means details of users will come
        return False
