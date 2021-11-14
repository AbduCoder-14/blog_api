from rest_framework import serializers
from .models import Post, Vote
from comments.serializers import CommentSerializer


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("title", "description", "image", "category")


class PostsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("title", "category")


class PostDetailSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(read_only=True, many=True)
    votes = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            "title",
            "description",
            "get_image",
            "get_thumbnail",
            "category",
            "votes",
            "comments",
        )

    def get_votes(self, post):
        return Vote.objects.filter(post=post).count()


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ("id",)


class VotesAnalyticsSerializer(serializers.ModelSerializer):
    post = serializers.SlugRelatedField(slug_field="title", read_only=True)

    class Meta:
        model = Vote
        fields = ("post", "created_at")
