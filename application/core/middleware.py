from django.shortcuts import redirect

class RedirectWWWMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host()
        if host.startswith("www."):
            return redirect(f"https://{host[4:]}{request.get_full_path()}", permanent=True)
        return self.get_response(request)