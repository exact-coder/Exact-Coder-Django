from django.shortcuts import redirect
from django.urls import reverse

class RestrictAdminMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self,request):
        if (
            not request.user.is_authenticated
            or (not request.user.is_superuser and not request.user.is_staff)
        ) and request.path.startswith('/admin'):
            return redirect(reverse('home'))
        response = self.get_response(request)
        return response
