from shortener.models import Link
from rest_framework import viewsets, permissions
from .serializers import LinkSerializer


class LinkViewSet(viewsets.ModelViewSet):
    queryset = pass
    permission_classes = [
        pass
    ]
    serializer_class = pass
    # Complete view set class implementation