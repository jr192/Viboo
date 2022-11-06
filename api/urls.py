from django.urls import path
from rest_framework import routers

from .views.create_building import BuildingsViewSet
from .views.retrieve_temperature import get_temperature

router = routers.DefaultRouter()


router.register("buildings", BuildingsViewSet, basename="buildings")
urlpatterns = [
    path("temperature/<int:building_id>/<str:room_id>", get_temperature),
    *router.urls,
]
