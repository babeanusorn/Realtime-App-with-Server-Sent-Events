from django.conf.urls import url
from channels.routing import URLRouter
from channels.http import AsgiHandler
from channels.auth import AuthMiddlewareStack
import django_eventstream

urlpatterns = [
    url(r'^message/events/', AuthMiddlewareStack(
        URLRouter(django_eventstream.routing.urlpatterns)
    ), {'channels': ['test-message']}),
    url(r'', AsgiHandler),
]