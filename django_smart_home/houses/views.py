from django.contrib.auth.models import User
from .models import House, Room, Device, LightAttributes, TvAttributes, ThermostatAttributes, DoorAttributes
from .creation_forms import HouseCreationForm, RoomCreationForm, DeviceTypeForm, \
    LightCreationForm, TvCreationForm, DoorCreationForm, ThermostatCreationForm
from .update_forms import HouseUpdateForm, RoomUpdateForm, DeviceTypeUpdateForm, LightUpdateForm, \
    ThermostatUpdateForm, TvUpdateForm, DoorUpdateForm
from .change_forms import ThermostatChangeForm, TvChangeForm, DoorChangeForm, LightChangeForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages


@login_required
def house_list(request):
    all_houses = House.objects.filter(user=request.user).all()
    return render(request, 'houses/house_list.html', {'houses': all_houses})


@login_required
def create_house(request):
    if request.method == 'POST':
        form = HouseCreationForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            messages.success(request, f'Your new house has been created')
            return redirect('house-list')
    else:
        form = HouseCreationForm()
    return render(request, 'houses/house_form.html', {'form': form, 'key': 'create'})


@login_required
def delete_house(request, pk):
    house = get_object_or_404(House, pk=pk)
    if house.user == request.user:
        house.delete()
        messages.success(request, 'Your house deleted successfully.')
    return redirect('house-list')


@login_required
def update_house(request, pk):
    house = get_object_or_404(House, pk=pk)
    form = HouseUpdateForm(request.POST, instance=house)
    if request.method == 'POST':
        if house.user == request.user and form.is_valid():
            form.instance.user = request.user
            form.save()
            messages.success(request, f'Your house has been updated')
            return redirect('house-list')
    return render(request, 'houses/house_form.html', {'form': form, 'key': 'update'})


@login_required
def house_detail(request, pk):
    house = get_object_or_404(House, pk=pk)
    if house.user == request.user:
        rooms = Room.objects.filter(house=house).all()
        return render(request, 'houses/house_detail.html', {'house': house, 'rooms': rooms})
    return redirect('login')


@login_required
def add_new_room(request, pk):
    house = get_object_or_404(House, pk=pk)
    if request.method == 'POST':
        form = RoomCreationForm(request.POST)
        if house.user == request.user and form.is_valid():
            form.instance.user = request.user
            form.instance.house = house
            form.save()
            messages.success(request, f'Your new room has been created')
            return redirect('house-detail', house.id)
    else:
        form = RoomCreationForm()
    return render(request, 'houses/room_form.html', {'form': form, 'key': 'create'})


@login_required
def update_room(request, pk, fk):
    house = get_object_or_404(House, pk=pk)
    room = get_object_or_404(Room, pk=fk)
    if request.method == 'POST':
        form = RoomUpdateForm(request.POST, instance=room)
        form.instance.house = house
        if room.house.user == request.user and form.is_valid():
            form.instance.house.user = request.user
            form.save()
            messages.success(request, f'Your room has been updated')
            return redirect('house-detail', house.id)
    else:
        form = RoomUpdateForm(instance=room)
        form.instance.house = house
        return render(request, 'houses/room_form.html', {'form': form, 'key': 'update'})


@login_required
def delete_room(request, pk, fk):
    room = get_object_or_404(Room, pk=fk)
    if room.house.user == request.user:
        room.delete()
        messages.success(request, 'Your room deleted successfully.')
    return redirect('house-detail', pk)


@login_required
def create_device(request, pk, fk):
    room = get_object_or_404(Room, pk=fk)
    if request.method == 'POST':
        device_type_form = DeviceTypeForm(request.POST)
        device_type_form.instance.user = request.user
        device_type_form.instance.room = room
        if device_type_form.is_valid():

            device_name = device_type_form.cleaned_data['name']
            device_type = device_type_form.cleaned_data['device_type']
            existing_device = Device.objects.filter(room=room, name=device_name, device_type=device_type).first()

            if existing_device is not None:
                messages.error(request, 'A device with this name and type is already exists in this room')
                return redirect('device-list', pk, fk)

            device = device_type_form.save()
            if device.device_type.type_name == 'Light':

                light_form = LightCreationForm(request.POST)
                if light_form.is_valid():
                    light_attributes = light_form.save(commit=False)
                    light_attributes.device = device
                    light_attributes.save()

            if device.device_type.type_name == 'Tv':
                tv_form = TvCreationForm(request.POST)
                if tv_form.is_valid():
                    tv_attributes = tv_form.save(commit=False)
                    tv_attributes.device = device
                    tv_attributes.save()
            if device.device_type.type_name == 'Door':
                door_form = DoorCreationForm(request.POST)
                if door_form.is_valid():
                    door_attributes = door_form.save(commit=False)
                    door_attributes.device = device
                    door_attributes.save()

            if device.device_type.type_name == 'Thermostat':
                thermostat_form = ThermostatCreationForm(request.POST)
                if thermostat_form.is_valid():
                    thermostat_attributes = thermostat_form.save(commit=False)
                    thermostat_attributes.device = device
                    thermostat_attributes.save()

            return redirect('device-list', pk, fk)

    else:
        device_type_form = DeviceTypeForm()
        light_form = LightCreationForm()
        tv_form = TvCreationForm()
        door_form = DoorCreationForm()
        thermostat_form = ThermostatCreationForm()

    return render(request, 'houses/device_form.html', {
        'device_type_form': device_type_form,
        'light_form': light_form,
        'tv_form': tv_form,
        'door_form': door_form,
        'thermostat_form': thermostat_form,
        'key': 'update'
    })


@login_required
def update_device(request, pk, fk, device_id):
    room = get_object_or_404(Room, pk=fk)
    device = get_object_or_404(Device, pk=device_id)

    device.room = room
    if request.method == 'POST':
        device_type_form = DeviceTypeUpdateForm(request.POST, instance=device)
        device_type_form.instance.user = request.user
        device_type_form.instance.room = room
        if device_type_form.is_valid():
            device_name = device_type_form.cleaned_data['name']
            device_type = device.device_type
            existing_device = Device.objects.filter(room=room, name=device_name, device_type=device_type).first()

            if existing_device != device:
                messages.error(request, 'A device with this name and type is already exists in this room')
                return redirect('device-list', pk, fk)

            device = device_type_form.save()
            if device.device_type.type_name == 'Light':
                light = get_object_or_404(LightAttributes, pk=device_id)
                light_form = LightUpdateForm(request.POST, instance=light)
                if light_form.is_valid():
                    light_attributes = light_form.save(commit=False)
                    light_attributes.device = device
                    light_attributes.save()
            if device.device_type.type_name == 'Tv':
                tv = get_object_or_404(TvAttributes, pk=device_id)
                tv_form = TvUpdateForm(request.POST, instance=tv)
                if tv_form.is_valid():
                    tv_attributes = tv_form.save(commit=False)
                    tv_attributes.device = device
                    tv_attributes.save()
            if device.device_type.type_name == 'Door':
                door = get_object_or_404(DoorAttributes, pk=device_id)
                door_form = DoorUpdateForm(request.POST, instance=door)
                if door_form.is_valid():
                    door_attributes = door_form.save(commit=False)
                    door_attributes.device = device
                    door_attributes.save()

            if device.device_type.type_name == 'Thermostat':
                thermostat = get_object_or_404(ThermostatAttributes, pk=device_id)
                thermostat_form = ThermostatUpdateForm(request.POST, instance=thermostat)
                if thermostat_form.is_valid():
                    thermostat_attributes = thermostat_form.save(commit=False)
                    thermostat_attributes.device = device
                    thermostat_attributes.save()

            return redirect('device-list', pk, fk)

    else:
        device_type_form = DeviceTypeUpdateForm(instance=device)
        light_form = LightUpdateForm()
        tv_form = TvUpdateForm()
        door_form = DoorUpdateForm()
        thermostat_form = ThermostatUpdateForm()

    return render(request, 'houses/device_update_form.html', {
        'device_type_form': device_type_form,
        'light_form': light_form,
        'tv_form': tv_form,
        'door_form': door_form,
        'thermostat_form': thermostat_form,
        'key': 'create'
    })


@login_required
def list_devices(request, pk, fk):
    house = get_object_or_404(House, pk=pk)
    room = get_object_or_404(Room, pk=fk)
    devices = Device.objects.filter(room=room).all()
    if room.house.user == request.user:
        return render(request, 'houses/device_list.html', {'house': house, 'room': room, 'devices': devices})
    return redirect('login')


@login_required
def delete_device(request, pk, fk, device_id):
    device = get_object_or_404(Device, pk=device_id)
    if device.room.house.user == request.user:
        device.delete()
        return redirect('device-list', pk, fk)

@login_required
def room_detail(request, pk, fk):
    room = get_object_or_404(Room, pk=fk)
    device_forms = {}

    def create_or_update_forms(device_type, form_class, attributes_model):
        devices = Device.objects.filter(room=room, device_type__type_name=device_type)
        for device in devices:
            attributes = attributes_model.objects.filter(device=device).first()
            form_key = f"{device_type}_{device.id}"
            form = form_class(instance=attributes, prefix=form_key)
            device_forms[form_key] = form

        if request.method == 'POST':
            form_key = request.POST.get('form_key')
            if form_key in device_forms:
                form = device_forms[form_key]
                updated_form = form.__class__(request.POST, request.FILES, instance=form.instance, prefix=form_key)
                if request.user == updated_form.instance.device.user and updated_form.is_valid():
                    updated_form.save()
                    messages.success(request, 'Device settings updated successfully.')
                else:
                    messages.error(request, 'Error updating device.')
                device_forms[form_key] = updated_form

    create_or_update_forms('Light', LightChangeForm, LightAttributes)
    create_or_update_forms('Tv', TvChangeForm, TvAttributes)
    create_or_update_forms('Thermostat', ThermostatChangeForm, ThermostatAttributes)
    create_or_update_forms('Door', DoorChangeForm, DoorAttributes)

    return render(request, 'houses/device_list_version_2.html', {
        'device_forms': device_forms,
        'room': room
    })
