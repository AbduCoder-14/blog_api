from django.urls import path
from .views import FollowerView, ListFollowerView


urlpatterns = [
    path("followers/", ListFollowerView.as_view()),
    path("follower/<int:pk>/", FollowerView.as_view()),
]
