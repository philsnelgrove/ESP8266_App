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

    def __str__(self):
        return (self.name)

    def is_online(self):
        return (self.connected)

    def device_id(self):
        return (self.id)

    def device_status(self):
        return self.status

    def device_led_status(self):
        return self.led_status
