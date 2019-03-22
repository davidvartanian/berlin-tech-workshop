from graphene_django import DjangoObjectType
import graphene
from .models import Link as LinkModel


class Link(DjangoObjectType):
    class Meta:
        model = LinkModel

class Query(graphene.ObjectType):
    links = graphene.List(Link)

    def resolve_links(self, info):
        return LinkModel.objects.all()

schema = graphene.Schema(query=Query)