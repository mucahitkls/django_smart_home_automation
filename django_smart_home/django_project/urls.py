"""
URL configuration for django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home import views as home_views
from users import views as user_views
from houses import views as house_views
from django.contrib.auth import views  as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_views.home, name='home-page'),
    path('about/', home_views.about, name='about-page'),


    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('profile/', user_views.profile, name='profile'),
    path('logout/', user_views.custom_logout, name='logout'),

    # Home paths
    path('houses/', house_views.house_list, name='house-list'),
    path('houses/add_house/', house_views.create_house, name='house-add'),
    path('houses/<int:pk>/', house_views.house_detail, name='house-detail'),
    path('houses/<int:pk>/delete', house_views.delete_house, name='house-delete'),
    path('houses/<int:pk>/update', house_views.update_house, name='house-update'),

    # Room paths
    path('houses/<int:pk>/add_room', house_views.add_new_room, name='room-add'),
    path('houses/<int:pk>/delete_room/<int:fk>', house_views.delete_room, name='room-delete'),
    path('houses/<int:pk>/update/<int:fk>', house_views.update_room, name='room-update'),
    path('houses/<int:pk>/details/<int:fk>', house_views.room_detail, name='room-detail'),


    # Device paths
    path('houses/<int:pk>/rooms/<int:fk>', house_views.list_devices, name='device-list'),
    path('houses/<int:pk>/rooms/<int:fk>/add_device', house_views.create_device, name='device-add'),
    path('houses/<int:pk>/rooms/<int:fk>/delete_device/<int:device_id>', house_views.delete_device, name='device-delete'),
    path('houses/<int:pk>/rooms/<int:fk>/update_device/<int:device_id>', house_views.update_device, name='device-update'),


]



