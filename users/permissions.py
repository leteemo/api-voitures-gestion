from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    """
    Permission pour autoriser uniquement les admins à effectuer certaines actions.
    """

    def has_permission(self, request, view):
        # Vérifier si l'utilisateur a le rôle 'admin'
        return request.user.is_authenticated and request.user.role == 'admin'
