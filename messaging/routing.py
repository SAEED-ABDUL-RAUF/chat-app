from django.urls import re_path, path

from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/group/(?P<group_name>\w+)/$", consumers.ChatConsumer.as_asgi()),
    re_path(r"ws/dm/@(?P<username>\w+)/$", consumers.PrivateChatConsumer.as_asgi()),
    # re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
]
