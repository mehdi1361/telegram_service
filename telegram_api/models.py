from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class Channel(models.Model):
    user = models.OneToOneField(User, related_name='user_channel')
    name = models.CharField(verbose_name=_('name'), max_length=50,default=None)
    url = models.CharField(verbose_name=_('telegram url'), max_length=100)
    description = models.TextField(verbose_name='channel description')
    create_date = models.DateTimeField(verbose_name=_('created date'),auto_now_add=True)
    # image = models.ImageField(verbose_name=_('image for channel'),null=True)

    class Meta:
        db_table='channel'

    def __str__(self):
        return self.name


class GemBox(models.Model):
    name = models.CharField(verbose_name='name', max_length=50,default=None)
    price = models.PositiveIntegerField(verbose_name=_('price'),default=100)
    sku = models.IntegerField(verbose_name=_('sku'),default=100,unique=True)

    class Meta:
        db_table = 'game_box'

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='user_profile')
    mobile_no = models.IntegerField(default=100,unique=True)
    gem_quantity = models.IntegerField(default=100,unique=True)
    create_date = models.DateTimeField(verbose_name=_('created date'),auto_now_add=True)

    class Meta:
        db_table = 'user_profile'

    def __str__(self):
        return self.user.username

class UserGemBox(models.Model):
    user = models.ForeignKey(UserProfile)
    gem_box = models.ForeignKey(GemBox)
    create_date = models.DateTimeField(verbose_name=_('created date'),auto_now_add=True)

    class Meta:
        db_table = 'user_gem_buy'
    
class UsedGem(models.Model):
    user = models.ForeignKey(UserProfile)
    gem_quantity = models.IntegerField(default=5, unique=True)
    create_date = models.DateTimeField(verbose_name=_('created date'),auto_now_add=True)

    class Meta:
        db_table = 'user_gem_used'
