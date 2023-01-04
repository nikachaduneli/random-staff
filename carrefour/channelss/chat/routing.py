from django.urls import re_path
from . import consumers

websocket_urlspatterns = [
    re_path(r'ws/socket-server/', consumers.Chat.as_asgi())
]