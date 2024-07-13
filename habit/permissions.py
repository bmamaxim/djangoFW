from rest_framework import permissions


class IsUser(permissions.BasePermission):
    """
    Класс прав доступа пользователя.
    """

    def has_object_permission(self, request, view, obj):
        message = "доступ только для пользователя."
        if obj.user == request.user:
            return True
        return False
