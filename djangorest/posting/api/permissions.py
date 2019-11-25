from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    # object level permission to only allow the use of the object to edit it
    # assumes the model instalnce has an owner attribute

    def has_object_permisson(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
        # Check permissions for read-only request
            return True
        return obj.owner == request.user
