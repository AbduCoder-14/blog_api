from rest_framework import serializers

from .models import Profile


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
            "phone",
            "bio",
            "skills",
        )
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        user = Profile.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            phone=validated_data["phone"],
            bio=validated_data["bio"],
            skills=validated_data["skills"],
        )
        return user


class GetProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = (
            "groups",
            "user_permissions",
            "is_superuser",
            "is_staff",
            "is_active",
        )
