from django.utils import timezone
from re import sub
from rest_framework.authtoken.models import Token
from .models import Profile


class UpdateLastActivityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        header_token = request.META.get("HTTP_AUTHORIZATION", None)
        if header_token is not None:
            try:
                token = sub("Token ", "", request.META.get("HTTP_AUTHORIZATION", None))
                token_obj = Token.objects.get(key=token)
                request.user = token_obj.user
            except Token.DoesNotExist:
                pass
            # This is now the correct user
            Profile.objects.filter(id=request.user.id).update(
                last_activity=timezone.now()
            )
