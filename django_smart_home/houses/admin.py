from django.contrib import admin
from .models import House, Room, DeviceType, Device, DoorAttributes, LightAttributes, ThermostatAttributes, TvAttributes

admin.site.register(House)
admin.site.register(Room)
admin.site.register(DeviceType)
admin.site.register(Device)
admin.site.register(DoorAttributes)
admin.site.register(LightAttributes)
admin.site.register(TvAttributes)
admin.site.register(ThermostatAttributes)

