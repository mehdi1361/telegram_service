from django.contrib import admin
from .models import Channel,GemBox,UserProfile, UserGemBox, UsedGem 
# Register your models here.

@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "url", "description", "create_date")
    list_editable = ("url","description")
    search_fields = ("name", "url")

@admin.register(GemBox)
class GemAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "sku")
    list_editable = ("name","price")
    search_fields = ("name", "sku")

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "mobile_no","gem_quantity", "create_date")
    list_editable = ("mobile_no","gem_quantity")
    search_fields = ("user", "mobile_no")

@admin.register(UserGemBox)
class UserGemBoxAdmin(admin.ModelAdmin):
    list_display = ("user", "gem_box", "create_date")
    list_editable = ("gem_box",)
    search_fields = ("user", "mobile_no")

@admin.register(UsedGem)
class UserGemBoxAdmin(admin.ModelAdmin):
    list_display = ("user", "gem_quantity","create_date")
    list_editable = ("gem_quantity",)
    search_fields = ("user", "gem_quantity")

