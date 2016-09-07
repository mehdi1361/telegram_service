from django.contrib import admin
from .models import Channel,GemBox,UserProfile 
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
