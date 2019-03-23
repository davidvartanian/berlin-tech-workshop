from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets, permissions
from shortener.models import Link
from .serializers import LinkSerializer


@api_view(['GET'])
@permission_classes((AllowAny, ))
def api_root(request):
    return JsonResponse({"Hello":"World"})


class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    permission_classes = [IsAuthenticated,]
    serializer_class = LinkSerializer
