from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Department, Trainee, Trainer, Violation
from .serializers import (
    DepartmentSerializer,
    TraineeSerializer,
    TrainerSerializer,
    ViolationSerializer,
)
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth import logout
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from .permissions import *


class DepartmentViewSet(viewsets.ModelViewSet):
    permission_classes = [TrainerPermission]  # Corrected spelling

    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=True
        )  # Set partial=True
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


class TraineeViewSet(viewsets.ModelViewSet):
    permission_classes = [TrainerPermission]  # Corrected spelling

    queryset = Trainee.objects.all()
    serializer_class = TraineeSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=True
        )  # Set partial=True
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


class TrainerViewSet(viewsets.ModelViewSet):
    permission_classes = [UserPermission]

    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=True
        )  # Set partial=True
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


@api_view(["POST"])
def register_user(request):
    if request.method == "POST":
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ViolationViewSet(viewsets.ModelViewSet):
    permission_classes = [TrainerPermission]  # Corrected spelling

    queryset = Violation.objects.all()
    serializer_class = ViolationSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=True
        )  # Set partial=True
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


## Login logout
class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})


class CustomLogout(APIView):
    def post(self, request, *args, **kwargs):
        try:
            request.user.auth_token.delete()
        except AttributeError:
            return Response(
                {"error": "User not authenticated"}, status=status.HTTP_400_BAD_REQUEST
            )
        logout(request)
        return Response(
            {"success": "Successfully logged out"}, status=status.HTTP_200_OK
        )
