from rest_framework import generics, permissions
from .models import Comment
from .serializers import CommentCreateSerializer


class CommentsCreatetView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
