from django.db import models
from django.conf import settings

class Profile(models.Model):
    class Meta:
        verbose_name = u'player_num'
        verbose_name_plural = u'player_num'
        verbose_name = u'room_name'
        verbose_name_plural = u'room_name'
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    player_num = models.IntegerField(default=0)
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    room_num = models.IntegerField(default=0)


