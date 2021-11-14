from rest_framework import generics, permissions
from .models import Profile
from .serializers import UserCreateSerializer, GetProfileSerializer


class UserCreateView(generics.ListCreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = Profile.objects.all()


class ProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = GetProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Profile.objects.filter(id=self.request.user.id)
