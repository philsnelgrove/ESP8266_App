from django.shortcuts import render
from django.http import HttpResponse
from ESP8266_Control.models import Device


def index(request):
    device_list = Device.objects.order_by('-id')[:5]
    output = ', '.join([q.name for q in device_list])
    return HttpResponse(output)
