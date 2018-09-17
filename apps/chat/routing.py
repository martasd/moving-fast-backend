import logging

from django.urls import path

from .consumer import ChatConsumer

logger = logging.getLogger(__name__)

websocket_urlpatterns = [
    path('ws/chat/<room_name>/', ChatConsumer),
]
