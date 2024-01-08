from rest_framework import permissions

class IsStudentUser(permissions.BasePermission):
    """
    Custom permission to allow only student users to create blogs.
    """

    def has_permission(self, request, view):
        # Check if the user is authenticated and is a student.
        return request.user.is_authenticated and request.user.is_student
