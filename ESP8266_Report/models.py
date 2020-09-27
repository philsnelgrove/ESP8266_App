from django.db import models
from ESP8266_Control.models import Device


class Report(models.Model):
    id = models.IntegerField(primary_key=True)
    device = models.ForeignKey(Device, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=3, default='0')
    event = models.CharField(max_length=200)

    def __str__(self):
        return (self.event)

    def report_id(self):
        return (self.id)

    def report_status(self):
        return self.status
