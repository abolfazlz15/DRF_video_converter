from rest_framework import permissions


class IsAuthor(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if obj:
            return bool(
                request.user.is_authenticated and obj.user == request.user
            )
