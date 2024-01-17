from django import forms
from .models import House, Room, Device, LightAttributes, ThermostatAttributes, TvAttributes, DoorAttributes


class LightChangeForm(forms.ModelForm):
    class Meta:
        model = LightAttributes
        fields = ['color', 'brightness', ]


class ThermostatChangeForm(forms.ModelForm):
    class Meta:
        model = ThermostatAttributes
        fields = ['current_temperature']


class TvChangeForm(forms.ModelForm):
    class Meta:
        model = TvAttributes
        fields = ['current_channel', 'current_volume']


class DoorChangeForm(forms.ModelForm):
    class Meta:
        model = DoorAttributes
        fields = ['lock_state']
