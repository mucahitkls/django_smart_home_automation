from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class House(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} House'


class Room(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)


class DeviceType(models.Model):
    type_name = models.CharField(max_length=100, unique=True, null=False)

    def __str__(self):
        return self.type_name


class Device(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='devices')
    device_type = models.ForeignKey(DeviceType, on_delete=models.CASCADE, related_name='devices')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='devices')
    name = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class LightAttributes(models.Model):
    device = models.OneToOneField(Device, on_delete=models.CASCADE, primary_key=True, related_name='light_attributes')
    color = models.CharField(max_length=50)
    brightness = models.IntegerField()

    def __str__(self):
        return f"Light Attributes for {self.device.name}"


class ThermostatAttributes(models.Model):
    device = models.OneToOneField(Device, on_delete=models.CASCADE, primary_key=True,
                                  related_name='thermostat_attributes')
    current_temperature = models.IntegerField()
    min_temperature = models.IntegerField()
    max_temperature = models.IntegerField()

    def __str__(self):
        return f"Thermostat Attributes for {self.device.name}"


class TvAttributes(models.Model):
    device = models.OneToOneField(Device, on_delete=models.CASCADE, primary_key=True, related_name='tv_attributes')
    current_channel = models.IntegerField()
    current_volume = models.IntegerField()
    max_channel = models.IntegerField()
    max_volume = models.IntegerField()

    def __str__(self):
        return f"TV Attributes for {self.device.name}"


class DoorAttributes(models.Model):
    device = models.OneToOneField(Device, on_delete=models.CASCADE, primary_key=True, related_name='door_attributes')
    lock_state = models.CharField(max_length=50)

    def __str__(self):
        return f"Door Attributes for {self.device.name}"
