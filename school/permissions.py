from rest_framework import permissions


class IsSameUser(permissions.BasePermission):
    """
    Custom permission to only allow same users of an edit it.
    """

    def has_object_permission(self, request, view, obj):

        return obj == request.user