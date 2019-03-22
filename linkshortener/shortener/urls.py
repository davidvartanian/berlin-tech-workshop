from rest_framework import routers
from .api import LinkViewSet
from django.conf.urls import url
from graphene_django.views import GraphQLView


router = routers.DefaultRouter()
router.register('api/links', LinkViewSet, 'links')


urlpatterns = router.urls + [
    # ...
    url(r'^graphql', GraphQLView.as_view(graphiql=True)),
]