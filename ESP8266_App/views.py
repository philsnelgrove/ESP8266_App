# from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from ESP8266_Control.models import Device
from ESP8266Server.Server import Logic


def index(request):
    ip = ""
    port = 9999
    command = ""
    data = ""
    # Logic.Handler.send_command_to_node(request, ip, port, command, data)

    device_list = Device.objects.order_by('-id')
    template = loader.get_template('ESP8266_App/index.html')
    context = {
        'device_list': device_list,
    }
    return HttpResponse(template.render(context, request))
