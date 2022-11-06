from rest_framework import serializers

from api.model.rooms import Rooms
from api.serializers.thermostats import ThermostatsSerializer


class RoomsSerializer(serializers.ModelSerializer):
    thermostats = ThermostatsSerializer(many=True)

    class Meta:
        model = Rooms
        fields = ["room_id", "thermostats"]
