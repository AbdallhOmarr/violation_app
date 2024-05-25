from rest_framework import serializers
from .models import Department, Trainee, Trainer, Violation
from rest_framework import serializers

from django.contrib.auth.hashers import make_password


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"


class TraineeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainee
        fields = "__all__"

        ## this is an example of how to create a validation in the backend for the API

    # def validate_academic_number(self, value):
    #     value_str = str(value)
    #     if len(value_str) != 9:
    #         raise serializers.ValidationError("Academic Number must be a 9-digit number")
    #     else:
    #         return value


class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = "__all__"

    # def validate_account_number(self, value):
    #     value_str = str(value)
    #     if len(value_str) != 7:
    #         raise serializers.ValidationError("Academic Number must be a 7-digit number")
    #     else:
    #         return value
    def create(self, validated_data):
        user = Trainer.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        # Hash the password if it's included in the validated data
        if "password" in validated_data:
            validated_data["password"] = make_password(validated_data["password"])
        return super().update(instance, validated_data)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = (
            "full_name",
            "mobile_number",
            "email",
            "account_number",
            "status",
            "user_type",
            "password",
            "is_staff",
            "is_trainer",
        )
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = Trainer.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        # Hash the password if it's included in the validated data
        if "password" in validated_data:
            validated_data["password"] = make_password(validated_data["password"])
        return super().update(instance, validated_data)


class ViolationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Violation
        fields = "__all__"
