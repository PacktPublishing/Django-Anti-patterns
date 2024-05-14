# Custom middleware to log request/response information
class RequestLoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Log request information
        response = self.get_response(request)
        # Log response information
        return response

# In settings.py, add middleware to the MIDDLEWARE setting
MIDDLEWARE = [
    # Other middleware classes
    'myapp.middleware.RequestLoggerMiddleware',
]
