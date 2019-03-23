from rest_framework import routers
from django.conf.urls import url
from graphene_django.views import GraphQLView
from .views import LinkViewSet


router = routers.DefaultRouter()
router.register('api/links', LinkViewSet, 'links')


urlpatterns = router.urls + [
    # ...
    url(r'^graphql', GraphQLView.as_view(graphiql=True)),
]