"""
ASGI config for app project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

import django
from channels.http import AsgiHandler
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter,URLRouter
import app.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
django.setup()

application = ProtocolTypeRouter({
	"http":AsgiHandler(),
	"websocket":AuthMiddlewareStack(
		URLRouter(
			app.routing.websocket_urlpatterns
		)
	),
})
