
from rest_framework.permissions import BasePermission

class ISAuthenticated(BasePermission):
    messeage = " The movies list will appear unless you are authenticated "

    def has_object_permission(self, request, view, obj):
        if request.user.auth or request.user == obj.user:
            return False
        return True
