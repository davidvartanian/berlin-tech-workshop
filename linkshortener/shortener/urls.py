from rest_framework import routers
from django.conf.urls import url
from graphene_django.views import GraphQLView
from .views import LinkViewSet, redirect_view


router = routers.DefaultRouter()
router.register('links', LinkViewSet, 'links')


urlpatterns = router.urls + [
    # ...
    url(r'^graphql', GraphQLView.as_view(graphiql=True)),
    url(r'^redirect/(.*)', redirect_view)
]