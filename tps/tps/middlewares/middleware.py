import re
from django.http import HttpResponseRedirect
from django.conf import settings


class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.exceptions = tuple(
            re.compile(url)
            for url in getattr(settings, "LOGIN_REQUIRED_URLS_EXCEPTIONS", [])
        )

    def __call__(self, request):
        if not request.user.is_authenticated:
            for url in self.exceptions:
                if url.match(request.path_info):
                    return self.get_response(request)
            return HttpResponseRedirect(f"{settings.LOGIN_URL}?next={request.path}")

        response = self.get_response(request)
        return response
