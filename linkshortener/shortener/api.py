from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from shortener.models import Link
from .serializers import LinkSerializer


class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link
    permission_classes = [
        IsAuthenticated,
    ]
    serializer_class = LinkSerializer
    # Complete view set class implementation
