from django.urls import path

from .views import UserCreateView, ProfileDetailView


urlpatterns = [
    path("register/", UserCreateView.as_view()),
    path("profile/<int:pk>/", ProfileDetailView.as_view()),
]
