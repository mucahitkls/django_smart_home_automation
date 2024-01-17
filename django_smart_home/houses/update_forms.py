from django import forms
from .models import House, Room, Device, LightAttributes, ThermostatAttributes, TvAttributes, DoorAttributes


class HouseUpdateForm(forms.ModelForm):
    class Meta:
        model = House
        fields = ['name']


class RoomUpdateForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'description']


class DeviceTypeUpdateForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['name', 'state']


class LightUpdateForm(forms.ModelForm):
    class Meta:
        model = LightAttributes
        fields = ['color', 'brightness', ]


class ThermostatUpdateForm(forms.ModelForm):
    class Meta:
        model = ThermostatAttributes
        fields = ['current_temperature', 'min_temperature', 'max_temperature']


class TvUpdateForm(forms.ModelForm):
    class Meta:
        model = TvAttributes
        fields = ['current_channel', 'current_volume', 'max_channel', 'max_volume']


class DoorUpdateForm(forms.ModelForm):
    class Meta:
        model = DoorAttributes
        fields = ['lock_state']