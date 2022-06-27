from rest_framework import permissions

#crear y personalizar permisos

class UpdateOwnProfile(permissions.BasePermission):
    """
    Permite al user actualizar su propiop perfil"""
    def has_object_permission(self, request, view, obj):
        """
            Checkea si el user tiene permisos y permite si el user puede actualizar su propio perfil
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.id == request.user.id