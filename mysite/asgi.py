"""
ASGI config for mysite project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from channels.routing import ProtocolTypeRouter, URLRouter, ChannelNameRouter

from django.core.asgi import get_asgi_application
from django.urls import re_path

from strawberry.channels import GraphQLHTTPConsumer, GraphQLWSConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django_application = get_asgi_application()

from api.schema import schema

websocket_urlpatterns = [
    re_path(r'graphql', GraphQLWSConsumer.as_asgi(schema=schema)),
]

print(websocket_urlpatterns)

# gql_http_consumer = GraphQLHTTPConsumer.as_asgi(schema=schema)
# gql_ws_consumer = GraphQLWSConsumer.as_asgi(schema=schema)

application = ProtocolTypeRouter(
    {
        'http': django_application,
        # 'http': URLRouter(
        #     [
        #         # re_path('^graphql', gql_http_consumer),
        #         re_path(
        #             '^', django_application
        #         ),
        #     ]
        # ),
        'websocket': URLRouter(websocket_urlpatterns),
    }
)