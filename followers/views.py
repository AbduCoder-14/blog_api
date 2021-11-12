from rest_framework import generics, permissions, views, response
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from .models import Follower
from .serializers import ListFollowerSerializer
from accounts.models import Profile


class ListFollowerView(generics.ListAPIView):
    serializer_class = ListFollowerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Follower.objects.filter(user=self.request.user)


class FollowerView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        user = get_object_or_404(Profile, id=pk)
        try:
            Follower.objects.create(subscriber=request.user, user=user)
            return response.Response(status=201)
        except IntegrityError:
            return response.Response(status=201)

    def delete(self, request, pk):
        sub = get_object_or_404(Follower, subscriber=request.user, user_id=pk)
        sub.delete()
        return response.Response(status=204)
