from rest_framework import permissions


class BlogPostPermissions(permissions.BasePermission):


    def has_object_permission(self, request, view, obj):
        """
        Define si el usuario puede realizar la acción sobre el objeto <obj>
        Un usuario puede borrar o actualizar un anuncio, si es superusuario o si el anuncio es suyo
        """
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_superuser or obj.owner == request.user