from django.db import models

from api.model.rooms import Rooms


class Thermostats(models.Model):
    device = models.CharField(max_length=256)
    temperature = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    room = models.ForeignKey(Rooms, on_delete=models.DO_NOTHING, null=True)
