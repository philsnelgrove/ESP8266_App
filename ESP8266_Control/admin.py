from django.contrib import admin
from .models import Device
from ESP8266_Report.models import Report

# Register your models here.
admin.site.register(Device)
admin.site.register(Report)
