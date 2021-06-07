"""
ASGI config for group_chat project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path

from chat.consumers import ChatConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'group_chat.settings')

application = get_asgi_application()

from channels.auth import AuthMiddlewareStack

ws_patterns = [
    path('ws/<str:room_name>/', ChatConsumer),
]

application=ProtocolTypeRouter(
    {
        'websocket':AuthMiddlewareStack(URLRouter(
            ws_patterns
        ))
    }
)
