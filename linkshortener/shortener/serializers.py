from rest_framework import serializers
from shortener.models import Link


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = pass
        fields = ""
    # Complete implementation of serializer class