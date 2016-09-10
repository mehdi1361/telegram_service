from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Channel,GemBox

class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ("user", "name", "url", "description", "create_date")

class GemBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = GemBox
        fields = ("name", "price", "sku")
