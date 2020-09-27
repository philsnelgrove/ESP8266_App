from django.db import models


class Device(models.Model):
    id = models.IntegerField
    name = models.CharField(max_length=200)
    mac_address = models.CharField(max_length=200)
    last_connected = models.DateTimeField('last connected')
    ip_address = models.CharField(max_length=20)
    status = models.CharField(max_length=3, default='0')
    connected = models.CharField(max_length=5, default='false')
    led_status = models.CharField(max_length=3, default='off')
