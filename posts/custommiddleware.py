from django.utils.deprecation import MiddlewareMixin
from django.urls import resolve
from django.http import Http404

#!CustomMiddlewareExample
class CustomMiddlewareExample(MiddlewareMixin):
    def process_request(self, request):
        ip = request.META.get('REMOTE_ADDR')
        path = resolve(request.path).url_name
        if not ip == '127.0.0.1' and path == 'post-list-create':
            raise Http404('No access for you')
        else:
            print('This path is ok')
        return None
