from django.shortcuts import render

from rest_framework.decorators import api_view, detail_route
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import views, authentication, permissions, authtoken
from rest_framework import serializers
from .models import Channel, GemBox
from .serializer import ChannelSerializer, GemBoxSerializer
from rest_framework import viewsets
# Create your views here.

class ChannelViewSet(viewsets.ModelViewSet):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer


class GemBoxViewSet(viewsets.ModelViewSet):
    queryset = GemBox.objects.all()
    serializer_class = GemBoxSerializer
