from django.db import models


class Rooms(models.Model):
    room_id = models.CharField(max_length=256)
    building = models.ForeignKey(
        "Buildings", on_delete=models.CASCADE, null=True, related_name="buildings_rooms"
    )
