from django.shortcuts import render

from rest_framework.decorators import api_view, detail_route
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import views, authentication, permissions, authtoken
from rest_framework import serializers
from .models import Channel, GemBox, UserProfile, UserGemBox, UsedGem
from .serializer import ChannelSerializer, GemBoxSerializer, UserProfileSerializer, UserGemBoxSerializer, UsedGemSerializer 
from rest_framework import viewsets
# Create your views here.

class ChannelViewSet(viewsets.ModelViewSet):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer


class GemBoxViewSet(viewsets.ModelViewSet):
    queryset = GemBox.objects.all()
    serializer_class = GemBoxSerializer

class UserGemBoxViewSet(viewsets.ModelViewSet):
    queryset = UserGemBox.objects.all()
    serializer_class = UserGemBoxSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class UsedGemViewSet(viewsets.ModelViewSet):
    queryset = UsedGem.objects.all()
    serializer_class = UsedGemSerializer




