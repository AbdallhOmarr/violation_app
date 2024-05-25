from rest_framework import permissions
from .models import Trainer


# print(f"{obj.account_number} - {request.user.account_number} - {(request.user.is_superuser)} ")


class UserPermission(permissions.BasePermission):
    forbidden_fields = [
        "id",
        "last_login",
        "account_number",
        "status",
        "is_active",
        "is_trainer",
        "user_type",
        "is_staff",
        "is_superuser",
        "user_permissions",
        "date_joined",
        "groups",
    ]

    def has_object_permission(self, request, view, obj: Trainer):

        if request.user.is_authenticated:
            if request.method in ["GET", "HEAD", "OPTIONS"]:
                # Allow only the obj owner or the superuser to view the data
                return obj.account_number == request.user.account_number

            elif request.method in ["POST", "PUT"]:
                # Allow only the object owner to modify the data or the superuser
                if obj.account_number == request.user.account_number:
                    # If the user is trying to modify their own account
                    # Check if any forbidden fields are present in the request data
                    for field in self.forbidden_fields:
                        print(f"field:{field} - {request.data}")
                        if field in request.data:
                            return (
                                request.user.is_superuser
                            )  # Deny permission if any forbidden field is present
                    return True
                else:
                    return request.user.is_superuser

            return request.user.is_superuser
        else:
            return False


class TrainerPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        ## how to solve the error from reteriving data without authenticated ?

        if request.user.is_authenticated:
            if request.user.is_trainer:
                return True

            return request.user.is_superuser
        else:
            return False
