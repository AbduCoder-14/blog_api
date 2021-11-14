from rest_framework import generics, permissions, mixins, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Post, Vote
from .filters import VoteAnalyticsFilter
from .serializers import (
    PostsListSerializer,
    PostSerializer,
    PostDetailSerializer,
    VoteSerializer,
    VotesAnalyticsSerializer,
)


class PostCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostsListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostsListSerializer


class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer


class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "pk"

    def get_queryset(self):
        queryset = Post.objects.filter(author=self.request.user)
        return queryset


class VoteCreateView(generics.CreateAPIView, mixins.DestroyModelMixin):
    serializer_class = VoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        post = Post.objects.get(pk=self.kwargs["pk"])
        return Vote.objects.filter(voter=user, post=post)

    def perform_create(self, serializer):
        user = self.request.user
        post = Post.objects.get(pk=self.kwargs["pk"])
        if self.get_queryset().exists():
            raise ValidationError("You have already voted for this post")
        serializer.save(voter=user, post=post)

    def delete(self, request, *args, **kwargs):
        if self.get_queryset().exists():
            self.get_queryset().delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise ValidationError("You did not voted for this post")


class VotesAnalyticsView(generics.ListAPIView):
    queryset = Vote.objects.all()
    serializer_class = VotesAnalyticsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = VoteAnalyticsFilter
