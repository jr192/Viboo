from django.contrib import admin

from api.model.buildings import Buildings
from api.model.rooms import Rooms
from api.model.thermostats import Thermostats

admin.site.register(Buildings)
admin.site.register(Rooms)
admin.site.register(Thermostats)
