from rest_framework import serializers
from shortener.models import Link


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = "__all__"
    # Complete implementation of serializer class
