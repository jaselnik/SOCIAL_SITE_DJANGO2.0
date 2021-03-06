 # home/routing.py
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'^ws/chat/(?P<room_name>[^/]+)/$', consumers.GlobChatConsumer),
    re_path(r'^ws/home/chat/(?P<room_name>[^/]+)/$', consumers.ChatConsumer)
]