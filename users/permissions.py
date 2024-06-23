from rest_framework import permissions


class IsUser(permissions.BasePermission):
    """
    Класс прав доступа для объектов.
    """

    def has_object_permission(self, request, view, obj):

        if obj.user == request.user:
            return True
        return False