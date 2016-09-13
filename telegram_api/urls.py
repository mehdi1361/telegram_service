from rest_framework.routers import DefaultRouter
from . import views
router = DefaultRouter()
router.register(r'channel', views.ChannelViewSet)
router.register(r'gembox', views.GemBoxViewSet)
router.register(r'profile', views.UserProfileViewSet)
router.register(r'usergem', views.UserGemBoxViewSet)
router.register(r'usedgem', views.UsedGemViewSet)
