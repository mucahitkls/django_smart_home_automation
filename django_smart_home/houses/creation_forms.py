from django import forms
from .models import House, Room, Device, LightAttributes, ThermostatAttributes, TvAttributes, DoorAttributes


class HouseCreationForm(forms.ModelForm):
    class Meta:
        model = House
        fields = ['name']


class RoomCreationForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'description']



class DeviceTypeCreationForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['name', 'device_type']


class DeviceTypeForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['device_type', 'name', 'state']


class LightCreationForm(forms.ModelForm):
    class Meta:
        model = LightAttributes
        fields = ['color', 'brightness']


class ThermostatCreationForm(forms.ModelForm):
    class Meta:
        model = ThermostatAttributes
        fields = ['current_temperature', 'min_temperature', 'max_temperature']


class TvCreationForm(forms.ModelForm):
    class Meta:
        model = TvAttributes
        fields = ['current_channel', 'current_volume', 'max_channel', 'max_volume']


class DoorCreationForm(forms.ModelForm):
    class Meta:
        model = DoorAttributes
        fields = ['lock_state']


