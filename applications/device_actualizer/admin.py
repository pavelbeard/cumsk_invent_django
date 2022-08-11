from django.contrib import admin
from . import models


# Register your models here.

@admin.register(models.Nodetable)
class SnmpcDevicesAdmin(admin.ModelAdmin):
    fields = ('node_id', 'address', 'label', 'description')


@admin.register(models.CiscoDs)
class EsmaDevicesAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Esmacards)
class EsmacardsAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Pingariumresults)
class PingariumresultsAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Hardwareinfo)
class HardwareinfoAdmin(admin.ModelAdmin):
    pass

