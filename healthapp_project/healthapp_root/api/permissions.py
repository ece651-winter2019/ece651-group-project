from rest_framework.permissions import BasePermission


class IsPatientUser(BasePermission):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_patient)


# TBD if this class is needed
class IsDoctorUser(BasePermission):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_doctor)
