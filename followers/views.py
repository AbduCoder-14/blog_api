from rest_framework import generics, permissions, mixins, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .models import Follower
from .serializers import ListFollowerSerializer, FollowerSerializer
from accounts.models import Profile


class ListFollowerView(generics.ListAPIView):
    serializer_class = ListFollowerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Follower.objects.filter(user=self.request.user)


class FollowerView(generics.CreateAPIView, mixins.DestroyModelMixin):
    serializer_class = FollowerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        subscriber = Profile.objects.get(pk=self.kwargs["pk"])
        return Follower.objects.filter(user=user, subscriber=subscriber)

    def perform_create(self, serializer):
        user = self.request.user
        subscriber = Profile.objects.get(pk=self.kwargs["pk"])
        if self.get_queryset().exists():
            raise ValidationError("You have already followed for this user")
        serializer.save(user=user, subscriber=subscriber)

    def delete(self, request, *args, **kwargs):
        if self.get_queryset().exists():
            self.get_queryset().delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise ValidationError("You did not followed for this user")
