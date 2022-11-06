import datetime

from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.model.thermostats import Thermostats
import statistics


@api_view(["GET"])
def get_temperature(self, building_id, room_id):
    created_time = datetime.datetime.now() - datetime.timedelta(minutes=15)

    result = list(
        Thermostats.objects.select_related("room")
        .select_related("buildings_rooms")
        .filter(room__room_id=room_id, room__building__building_id=building_id)
        .filter(date_created__gte=created_time)
        .values_list("temperature", flat=True)
    )
    if result:
        return Response({"Temperature": statistics.mean(result)})
    else:
        return Response("Sorry, does not exist records in the last 15 minutes")
