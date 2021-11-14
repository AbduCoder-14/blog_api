from django.urls import path

from .views import (
    PostCreateView,
    PostRetrieveUpdateDestroyView,
    PostDetailView,
    PostsListView,
    VoteCreateView,
    VotesAnalyticsView,
)


urlpatterns = [
    path("", PostsListView.as_view()),
    path("post/create/", PostCreateView.as_view()),
    path("post/edit/<int:pk>/", PostRetrieveUpdateDestroyView.as_view()),
    path("post/<int:pk>/", PostDetailView.as_view()),
    path("post/<int:pk>/vote/", VoteCreateView.as_view()),
    path("analytics/", VotesAnalyticsView.as_view()),
]
