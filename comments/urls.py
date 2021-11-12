from django.urls import path
from .views import CommentsCreatetView


urlpatterns = [
    path("comment/create/", CommentsCreatetView.as_view()),
]
