from django.db import models


class Buildings(models.Model):
    building_id = models.IntegerField()
    timestamp = models.DateTimeField()
