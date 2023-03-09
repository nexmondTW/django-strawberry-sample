
from django.urls import path
from strawberry.django.views import GraphQLView
from api.schema import schema

urlpatterns = [
    path('graphql/', GraphQLView.as_view(schema=schema, subscriptions_enabled=True)),
]
