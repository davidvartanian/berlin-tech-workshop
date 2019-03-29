import logging

from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets
from .models import Link
from .serializers import LinkSerializer
from django.shortcuts import redirect, get_object_or_404


@api_view(['GET'])
@permission_classes((AllowAny, ))
def api_root(request):
    return JsonResponse({"Hello": "World"})


class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    permission_classes = [IsAuthenticated, ]
    serializer_class = LinkSerializer


@api_view(['GET'])
@permission_classes((AllowAny, ))
def redirect_view(request, token):
    link = get_object_or_404(Link, token=token)
    response = redirect(link.url)
    return response
