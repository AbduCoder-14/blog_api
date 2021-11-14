from rest_framework import serializers
from .models import Follower
from accounts.models import Profile


class UserByFollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("id", "username")


class ListFollowerSerializer(serializers.ModelSerializer):
    subscriber = UserByFollowerSerializer(read_only=True)

    class Meta:
        model = Follower
        fields = ("subscriber",)


class FollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        fields = ("id",)
