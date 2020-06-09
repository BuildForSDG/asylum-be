from rest_framework import permissions


class IsSpecialistOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return not request.user.is_patient
