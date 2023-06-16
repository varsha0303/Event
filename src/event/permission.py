from rest_framework.permissions import BasePermission
from user import choices

class EventPermission(BasePermission):
    def has_permission(self, request, view):
        if view.action in ('create', 'update', 'partial_update', 'destroy'):
            return request.user.user_type == choices.ADMIN
        return True


class BookingPermission(BasePermission):
    def has_permission(self, request, view):
        if view.action in ('update', 'partial_update', 'destroy'):
            return request.user.user_type == choices.ADMIN
        if view.action in ('create'):
            return request.user.is_authenticated
        return request.user.is_authenticated
