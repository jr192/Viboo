from rest_framework import serializers

from api.model.thermostats import Thermostats


class ThermostatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thermostats
        fields = ["device", "temperature"]
