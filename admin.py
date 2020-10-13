from django.contrib import admin
from ESP8266_Control.models import Device
from ESP8266_Report.models import Report

# Register your models here.
admin.site.register(Device)
admin.site.register(Report)
