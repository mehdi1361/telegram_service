from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Channel, GemBox, UserProfile, UserGemBox, UsedGem

class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ("user", "name", "url", "description", "create_date")

class GemBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = GemBox
        fields = ("name", "price", "sku")

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ("user", "mobile_no", "gem_quantity", "create_date")

class UserGemBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGemBox
        fields = ("user", "gem_box", "create_date")

class UsedGemSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ("user", "gem_quantity", "create_date")




