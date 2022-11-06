from rest_framework import serializers

from api.model.buildings import Buildings
from api.model.rooms import Rooms
from api.model.thermostats import Thermostats
from api.serializers.rooms import RoomsSerializer


class BuildingsSerializer(serializers.ModelSerializer):
    rooms = RoomsSerializer(many=True)

    class Meta:
        model = Buildings
        fields = ["building_id", "timestamp", "rooms"]

    def create(self, validated_data):
        room_data = validated_data.pop("rooms")
        building = Buildings.objects.create(**validated_data)
        for room in room_data:
            obj = Rooms.objects.create(building=building, **room)
            for thermo in room.pop("thermostats"):
                Thermostats.objects.create(room=obj, **thermo)

        return building
