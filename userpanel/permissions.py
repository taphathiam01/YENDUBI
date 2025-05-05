from rest_framework.permissions import BasePermission

class IsClientUser(BasePermission):
    """
    Autorise uniquement les utilisateurs avec le rôle 'client'.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and getattr(request.user, 'role', None) == 'client'
