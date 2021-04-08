from django.contrib import admin
from django.utils.translation import gettext as _

from .models import Appointment, Client, Service


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['user', 'service', 'client', 'reserved_at']
    list_filter = ['reserved_at']


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['_full_name', '_phone']

    def _full_name(self, obj):
        return obj.full_name

    _full_name.short_description = _("Имя")

    def _phone(self, obj):
        return obj.format_phone()

    _phone.short_description = _("Teлефон")


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'is_active']