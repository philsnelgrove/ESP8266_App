from django.db import models


class Device(models.Model):
    id = models.IntegerField
    name = models.CharField(max_length=200)
    mac_address = models.CharField(max_length=200)
    last_connected = models.DateTimeField('last connected')
    ip_address = models.CharField(max_length=20)
